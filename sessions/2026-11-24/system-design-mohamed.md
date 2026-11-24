# AI Sales Employee — system design in Mohamed's words (living spec)
Started 2026-11-24 in Claude Code. Mohamed is describing the system in parts; this file collects them. When he finishes, it gets applied to PLAYBOOK.md and agents/.

## Part 1 — ICP (2026-11-24) → applied to CONTEXT.md §3
- A1: big media buyers (500K+ documented sales for a brand + content gap).
- A2: service solopreneurs ~18–27 (AI automation / AI implementation, B2B sales, service providers) who need content to get more clients. Clients/offer/case studies not required. Course sellers OK. Not those whose audience is students or beginners.
- B: domain experts ~30–45 (consultants, coaches, accountants, tax, lawyers, language instructors, clinic owners) with an 11–50 company (smaller still a strong signal), whose expertise beats how they look online.

## Part 2 — Offer ladder (2026-11-24) → applied to CONTEXT.md §4
1. Free content (YouTube + Reels) for those who can't pay.
2. Program / academy: they execute alone under Mohamed's supervision.
3. Consultation (paid session).
4. 1:1 with Mohamed: highest, most expensive.
Prices as in CONTEXT §4 until Mohamed changes them.

## Part 3 — The agents (2026-11-24)
1. **Agent 1, Prospect finder:** searches for prospects in the segments above.
2. **Agent 2, Qualifier:** filters Agent 1's list down to real potential clients.
3. **Agent 3, Conversation agent:** opens and runs the conversation with qualified prospects.
   - Drafts the messages (Mohamed's tone and structure; he will give the exact message method, structure and tone of voice later).
   - Goal: get the prospect to tell us his problem so we can help. **We don't sell at all in chat.**
   - From his answers and problems, judge which step on the offer ladder fits.
   - Then a friendly recommendation to book a Discovery Call. On the call Mohamed understands the problem in depth and talks about the right offer.
   - **Follow-ups are Agent 3's job too** (Mohamed, 2026-11-24): same tone of voice, one agent to train. First follow-up 3–4 days after the first message; if the prospect replies, no follow-up, the conversation just continues.
4. **Agent 4, Head of Sales** (Mohamed, 2026-11-24): supervises the whole process; holds the full structure; runs and corrects the agents; sends Mohamed anything urgent; weekly reports on the sales team and the process; prescriptive: forecasts + recommendations on what to improve and how, based on results and reports.
   - **Booked call = URGENT** (Mohamed, 2026-11-24): Agent 4 sends Mohamed all the prospect's data, the full problem, the suggested offer and why.
→ Applied 2026-11-24: `agents/1-prospect-finder.md`, `2-qualifier.md`, `3-conversation-agent.md`, `4-head-of-sales.md`, new `agents/README.md`, PLAYBOOK §3. Old team archived in `archive/agents-v1/`.

### Open (Mohamed will continue)
- Message method, structure, tone of voice for Agent 3.
- A2 economics: can a solopreneur afford 1:1, or is the program the fit?
- Anything after the call: call prep, proposal, outcome tracking (today S4, S5, S6).
- Follow-up count after the first one, spacing, when to stop.
- Where the agents run and how Mohamed approves and sends.

### Claude's notes for the discussion
- Recommendation on Agent 4: merge follow-up into Agent 3. Reasons: it is the same thread and the same voice; Agent 3 already knows what was said; two agents on one chat risk sending twice or contradicting; a follow-up is just "the next message when there's no reply", one scheduled step of the conversation. Booked calls are then tracked by the call-prep step, not a separate follow-up agent.
- In Mohamed's description, "if he replies, Agent 2 continues the conversation" most likely means Agent 3 (the conversation agent). Confirm.
- Mapping to today's `agents/` files: Agent 1 = P1, Agent 2 = P2, Agent 3 = W1 + S1 + S3 (+ S2 if merged), Agent 4 = S2. TL, S4, S5, S6 wait for the rest of the design.

## Part 4 — First message: value first (thinking aloud, 2026-11-24, NOT final)
Mohamed: the first message must make them link him to big value immediately; founders have no time to chat, they want "what will you give me". He wants to give the free value directly. Also keep Yassin's winning messages and techniques (opener A got ~11 replies from ~22 media buyers).
Formats proposed by Claude to test (see chat 2026-11-24): F1 = Yassin's winning opener compressed (proof number + gap + ready asset + yes/no); F2 = the value itself inside the message (one usable insight or ready hook + a question); F3 = Mohamed's best-ever message (ready free video, "whether we work together or not").

## Part 5 — Two outreach tracks (Mohamed, 2026-11-24)
- **Cold outreach:** enters with the value directly in the first message, for the highest reply rate. No "shall I send it?", no file or link, no pitch. (Formats F1/F3 with "أبعتهولك؟" are dropped; F2, value inside the message, is the cold direction.)
- **Warm / hot track:** a second part of sales, same Agent 3, for people who are warmer than cold. Mohamed will define it next.
- Style fix: no commas/punctuation between sentences (that's what he meant by "الفواصل").

## Part 6 — Personalized video outreach without filming (thinking aloud, 2026-11-24)
Mohamed wants to keep personalized videos (Loom-style) in outreach because they show real study of the prospect, but without spending filming time; ideally the system makes the video itself in his voice.
Options laid out by Claude (chat 2026-11-24):
- A. Faceless screen-review video, fully automatic: Agent 3 writes a 60–90 s script → screenshots of the prospect's public profile/posts (Chrome) → narration in Mohamed's cloned voice (voice-clone service, his consent, trained on clean audio from his existing videos) → rendered with captions in his brand (OpenMontage/ffmpeg on the laptop) → MP4. Mohamed only approves the script (~1–2 min per video).
- B. AI avatar of his face + cloned voice (personalized avatar video tools). Fastest to look "on camera", highest risk of feeling fake.
- C. Hybrid: Mohamed records ONE short real intro once, reused; the personalized part is generated (A).
Risks: Egyptian-dialect quality of cloned voices must be tested; if a prospect spots AI, trust drops (Mostafa already called out AI copy). His own rule: no unexpected files/links, yet his best message was a direct free video. Needs a pilot on 1–3 prospects before any rollout.
→ Pilot built 2026-11-24 (option A): `video-outreach/` (README, build_video.py, pilot-khaled-shetewy). 67-second video, placeholder Egyptian voice, zoom boxes on his bio and radio show, captions in Cairo. Waiting for Mohamed's review and the voice-clone decision.
→ 2026-11-24: Mohamed wanted videos like his real Looms (islam.mp4, louai.mp4, mr ahmed, SARI, sherif, mr.ibrahim in D:\OUTREACH): his face, his voice, his whiteboard explanation style, generated automatically. Claude can't clone his face/look locally; that needs a third-party avatar service Mohamed signs up for himself. Mohamed: cancel the video idea for now, continue on the agents. The pilot files stay in `video-outreach/` (paused).
