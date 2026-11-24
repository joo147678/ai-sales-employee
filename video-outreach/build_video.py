"""Personalized outreach video builder (pilot, 2026-11-24).

Usage (run from anywhere):
  <venv python> build_video.py <prospect-folder>

The prospect folder holds:
  script.json   segments: visual (profile | grid | idea), box [x0,y0,x1,y1] on the cropped image, text, optional card
  raw/profile.jpg, raw/grid.jpg   full Chrome screenshots of the prospect's public profile
Output: <prospect-folder>/out/video.mp4 (1080x1920, captions in Cairo, Builtbyjoo colours).

Voice: Microsoft edge-tts ar-EG-ShakirNeural as a placeholder. Swap synth() for Mohamed's cloned voice later.
"""
import asyncio, json, os, re, subprocess, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
W, H, FPS = 1080, 1920, 30
BG = (18, 18, 18)
ORANGE = (255, 102, 0)
VOICE = "ar-EG-ShakirNeural"
# crops of the 1536x695 Chrome screenshot that remove Mohamed's own sidebar and Messages box
CROPS = {"profile": (400, 40, 1110, 475), "grid": (197, 45, 1323, 420)}


def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(r.stderr[-3000:])
        raise SystemExit("ffmpeg failed")


async def synth(text, mp3_path):
    import edge_tts
    words = []
    com = edge_tts.Communicate(text, VOICE, rate="+4%", boundary="WordBoundary")
    with open(mp3_path, "wb") as f:
        async for chunk in com.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                words.append((chunk["offset"] / 1e7, (chunk["offset"] + chunk["duration"]) / 1e7, chunk["text"]))
    return words


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout.strip()
    return float(out)


def still(folder, seg, i):
    img = Image.new("RGB", (W, H), BG)
    if seg["visual"] in CROPS:
        shot = Image.open(os.path.join(folder, "raw", seg["visual"] + ".jpg")).convert("RGB").crop(CROPS[seg["visual"]])
        box = seg.get("box")
        if box:
            # zoom into the highlighted area so it is readable on a phone
            m = 30
            region = (max(0, box[0] - m), max(0, box[1] - m), min(shot.width, box[2] + m), min(shot.height, box[3] + m))
            shot = shot.crop(region)
            box = [box[0] - region[0], box[1] - region[1], box[2] - region[0], box[3] - region[1]]
        target_w = 1040
        scale = target_w / shot.width
        if shot.height * scale > 1000:
            scale = 1000 / shot.height
        shot = shot.resize((int(shot.width * scale), int(shot.height * scale)), Image.LANCZOS)
        x0 = (W - shot.width) // 2
        y0 = 300 + (1000 - shot.height) // 2
        img.paste(shot, (x0, y0))
        d = ImageDraw.Draw(img)
        d.rectangle([x0 - 4, y0 - 4, x0 + shot.width + 3, y0 + shot.height + 3], outline=(60, 60, 60), width=4)
        if box:
            bx = [int(v * scale) for v in box]
            d.rectangle([x0 + bx[0], y0 + bx[1], x0 + bx[2], y0 + bx[3]], outline=ORANGE, width=10)
    p = os.path.join(folder, "work", f"still_{i}.png")
    img.save(p)
    return p


def clean(t):
    # Mohamed's rule: no commas or punctuation between sentences
    return re.sub(r"[،,.:؛]", "", t).strip()


def ass_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def main(folder):
    folder = os.path.abspath(folder)
    os.makedirs(os.path.join(folder, "work"), exist_ok=True)
    os.makedirs(os.path.join(folder, "out"), exist_ok=True)
    spec = json.load(open(os.path.join(folder, "script.json"), encoding="utf-8"))
    segs = spec["segments"]
    events, parts, t0 = [], [], 0.0
    for i, seg in enumerate(segs):
        mp3 = os.path.join(folder, "work", f"seg_{i}.mp3")
        words = asyncio.run(synth(seg["text"], mp3))
        dur = duration(mp3) + 0.25
        png = still(folder, seg, i)
        mp4 = os.path.join(folder, "work", f"seg_{i}.mp4")
        frames = int(dur * FPS)
        run(["ffmpeg", "-y", "-loop", "1", "-i", png, "-i", mp3,
             "-vf", f"scale=2160:3840,zoompan=z='min(1+on/{frames}*0.05,1.05)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}",
             "-af", "apad", "-t", f"{dur:.3f}", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS),
             "-c:a", "aac", "-ar", "48000", "-ac", "2", mp4], folder)
        parts.append(mp4)
        # captions: chunks of up to 4 words
        chunk = []
        for w in words:
            chunk.append(w)
            if len(chunk) == 4:
                events.append((t0 + chunk[0][0], t0 + chunk[-1][1], "Cap", " ".join(c[2] for c in chunk)))
                chunk = []
        if chunk:
            events.append((t0 + chunk[0][0], t0 + chunk[-1][1], "Cap", " ".join(c[2] for c in chunk)))
        if seg.get("card"):
            card = r"\N".join(seg["card"].split("\n"))
            events.append((t0, t0 + dur, "Card", card))
        t0 += dur
    total = t0
    name = spec.get("header", "")
    events.append((0, total, "Head", name or "فيديو مخصوص لحضرتك"))
    events.append((total - 4, total, "End", "محمد يوسف  |  @builtbyjoo"))

    with open(os.path.join(folder, "work", "list.txt"), "w", encoding="utf-8") as f:
        for p in parts:
            f.write(f"file '{p.replace(os.sep, '/')}'\n")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "work/list.txt", "-c", "copy", "work/joined.mp4"], folder)

    ass = ["[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "WrapStyle: 0", "",
           "[V4+ Styles]",
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           "Style: Cap,CairoBB,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,4,0,2,60,60,330,1",
           "Style: Head,CairoBB,52,&H000066FF,&H000066FF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,0,0,8,60,60,150,1",
           "Style: Card,CairoBB,78,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,0,0,5,80,80,0,1",
           "Style: End,CairoBB,54,&H000066FF,&H000066FF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,0,0,2,60,60,140,1",
           "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for s, e, style, text in events:
        text = clean(text) if style == "Cap" else text
        ass.append(f"Dialogue: 0,{ass_time(s)},{ass_time(e)},{style},,0,0,0,,{text}")
    open(os.path.join(folder, "work", "subs.ass"), "w", encoding="utf-8-sig").write("\n".join(ass))

    fonts_rel = os.path.relpath(FONT_DIR, folder).replace(os.sep, "/")
    run(["ffmpeg", "-y", "-i", "work/joined.mp4", "-vf", f"ass=work/subs.ass:fontsdir={fonts_rel}",
         "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-c:a", "aac", "-b:a", "160k",
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "out/video.mp4"], folder)
    print(f"done: {os.path.join(folder, 'out', 'video.mp4')}  ({total:.1f}s)")


if __name__ == "__main__":
    main(sys.argv[1])
