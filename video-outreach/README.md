# Video outreach — personalized videos without filming (pilot 2026-11-24)

A 60–90 s vertical video per prospect: his own public profile on screen, orange boxes + zoom on what we talk about, captions in Cairo, narration in Mohamed's voice. Mohamed only approves the script.

## Pipeline
1. **Screenshots** (Agent 1/2 or Agent 3, Claude in Chrome, public pages only): profile header + posts grid, saved as `<prospect>/raw/profile.jpg` and `raw/grid.jpg`. The crop removes Mohamed's own sidebar and Messages box.
2. **Script** (Agent 3, Mohamed's voice, CONTEXT + VOICE rules): `<prospect>/script.json`, 5–7 segments: greeting → what's strong (fact from his profile) → the gap → one free idea he can apply tomorrow → what changes → "free, whether we work together or not". Facts only from his public profile or the sheet; sources listed in the file.
3. **Mohamed approves the script** (1–2 min).
4. **Render** on the laptop: `"D:\content app\OpenMontage-main\OpenMontage-main\.venv\Scripts\python.exe" build_video.py <prospect-folder>` → `<prospect>/out/video.mp4` (about 1 minute to render).
5. **Mohamed sends** the video as a file with the cold message (CONTEXT/VOICE rules).

## Files
- `build_video.py`: the renderer (edge-tts narration with word timings → stills with zoom boxes → ffmpeg → ASS captions).
- `fonts/CairoBB.ttf`: Cairo Bold (Arabic + Latin merged from the OpenMontage Remotion fonts, OFL).
- `pilot-khaled-shetewy/`: first pilot (Segment B, tax consultant, sheet row 96).

## Voice
- Pilot uses a placeholder Egyptian male voice (Microsoft `ar-EG-ShakirNeural` via edge-tts). It is NOT Mohamed's voice.
- To use Mohamed's own voice: a voice-cloning service account (Mohamed creates it himself and gives consent), trained on 3–5 minutes of clean audio from his existing videos; then swap `synth()` in `build_video.py` for that service. Test the Egyptian dialect quality before any real send.

## Rules
- Public pages only; never open DMs; never Follow / Like / Message.
- Never invent a number, client or claim. Every fact in the script has a source in `script.json`.
- Nothing is sent by the system. Mohamed sends.
