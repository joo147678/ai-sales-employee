# HANDOFF — where we stopped

Last updated: 2026-11-24 (Claude chat session). Full chat summary: `sessions/2026-11-21/chat-context-export.md`. Notes: `sessions/2026-11-21/session-notes.md`.

## Status
- The AI Sales Employee has been stopped since 2026-11-11 (ChatGPT credits ran out, and the AI kept misreading the ICP and positioning).
- Yassin is stopped. Mohamed sends every message and owns every conversation.
- 2026-11-21: reviewed all 34 prospect chats (29 Instagram + 5 WhatsApp): 11 replies, 9 audits sent, 0 calls.
- Added `CONTEXT.md` as the single source of truth. Updated `PLAYBOOK.md`: media buyers are ICP, partnerships are out of scope, new month-to-month offers, a price-question rule, and storage moved to this folder + GitHub.
- Google Drive retired; its 17 docs are copied to `archive/google-drive/`.

## Decisions made 2026-11-21
- Media buyers / performance marketers are ICP (Segment A) only with EGP 500K+ documented sales for a brand AND a content gap (see CONTEXT §3).
- Partnerships/collabs are a separate track, not part of this employee.
- All offers are month-to-month. 1:1 is EGP 40K/month, all-inclusive, with a payment due at the start of each month.
- Proof "1M views + EGP 132K client sales in 5 months" is confirmed.
- Storage: this folder + GitHub repo `joo147678/ai-sales-employee`. No Google Drive.

## Added 2026-11-21 (evening)
- Sales team built: `agents/` (TL Senior Sales Team Leader + P1, P2, W1 Copywriter, S1–S6), shared `state/team-board.md`, `state/inbox/`, `state/alerts.md`, `state/run-log.md`.
- `VOICE.md` (Mohamed's voice) and `messages/library.md` (what worked/failed, from 34 chats + Yassin's CRM).
- Sheet exports archived: `archive/prospects-database-export-2026-11-21.md`, `archive/yassin-crm-export-2026-11-21.csv`.
- Schedules designed (P1/P2 24/7; others Sat–Thu, Friday off) but NOT created yet. Waiting for Mohamed's outreach strategy + where to run (see open item 3).

## Open / next
1. DONE 2026-11-21: pushed to private repo https://github.com/joo147678/ai-sales-employee (branch main). Keep D: folder and repo in sync.
2. Mohamed shares the rest of the system changes he has in mind (he said he'd list them). Apply them to PLAYBOOK/CONTEXT.
3. Decide where the agents run now (Claude Code / Codex / scheduled tasks) and reconnect them to this folder + repo instead of Drive.
4. Warm leads waiting for action (details in `sessions/2026-11-21/outreach-analysis.md`): Ahmed Hussein (asked price), Mostafa Mansour, AbdulRahman Dawood, Ahmed Ebrahem (busy, fine), Aser, Nermeen Edrees (workshop on Nov 28).
5. DONE 2026-11-24: Yassin's Nov 13 batch (14 names) added to the Prospects sheet, rows 97–110, with real status and next step (all media buyers marked '500K NOT verified').

## Added 2026-11-24 (Claude Code)
- Folder moved: `D:\OUTREACH\ai-sales-employee` → `D:\ai sales employee` (laptop tasks, PLAYBOOK, AGENTS, memory updated). This local folder is NOT a git checkout: sync to GitHub `joo147678/ai-sales-employee` must be done separately.
- Yassin's week 1 + week 2 reports analysed → `sessions/2026-11-24/yassin-reports-insights.md` (2 weeks: ~54 msgs → ~10 replies → ~8 audits/Looms → 0 calls; the leak is reply→call).
- Team board: sheet rows filled, overdue leads flagged (all 11-22 actions missed; Nermeen's workshop is 11-28).
- All automation still PAUSED: cloud routines (Daily Brief trig_01Wh4prEhuFQWuZpWVAMDgC6, Hourly Watcher trig_01Wa1oEe4KXVtjE8CfwffwRR, Prospecting trig_01DX26Fsp8obXD6wzN1A3HWy) and laptop task ai-sales-prospecting. Note: the cloud routines still read the retired Google Drive folder; they must be re-pointed before re-enabling.
- Mohamed is sending all WhatsApp + Instagram lead chats for a bigger analysis (save them to `sessions/2026-11-24/chats/`).

## Next
1. Mohamed decides: step after a reply (free 10-min call vs 2K session vs both), segment focus (A only or A+B), daily send capacity, where the agents run.
2. Analyse the full chat set when it arrives; update `messages/library.md`, `learning-log.md`, team board.
3. Overdue warm leads (team board): draft the messages for Mohamed in his voice (Ahmed Hussein price answer, Mostafa Reel script, Dawood question, Nermeen 3 hooks before 11-26).
- 2026-11-24 (later): Mohamed defined the ICP (A1 big media buyers, A2 service solopreneurs ~18–27, B domain experts ~30–45 with a company), the offer ladder (free content → program → consultation → 1:1) and the team: 4 agents (Prospect Finder, Qualifier, Conversation Agent with all follow-ups, Head of Sales). Applied to CONTEXT §3–4, PLAYBOOK §3, `agents/`. Old 10-agent team archived. Spec: `sessions/2026-11-24/system-design-mohamed.md`.
- Still to come from Mohamed: Agent 3 message method/structure/tone; follow-ups after the first one; where the agents run; A2 economics.
- GitHub: the folder is now a git repo linked to `joo147678/ai-sales-employee`; commits are local. Push was blocked by auto mode (prospect personal data): Mohamed runs `git push -u origin main` himself.
- 2026-11-24 (end of day): all open design items closed by Mohamed: 5 agents (1 Finder, 2 Qualifier, 3 Account Analyst on `analysis/METHOD.md`, 4 Conversation, 5 Head of Sales); follow-ups day 3 + day 6 then Nurture; cold = from the pipeline; Agent 4 discusses the problem and brings the call idea only at the end; A2 → 1:1 or academy; cloud 24/6, Friday off.

## Cloud team (live since 2026-11-24)
All in the cloud (environment Default), clone this GitHub repo, write state back to `main`. Sat–Thu, Friday off (each run checks the Cairo day and stops on Friday). Times are Cairo.
| Routine | When | Does | ID |
|---|---|---|---|
| Sales Desk (Agents 4+5) | every 2h 08:15–00:15 | sync Message Queue, Gmail/Calendly, Calendar, Fathom; drafts + QA -> Message Queue; urgent alerts + Call Files | trig_01FB5rEvPkAs4TAvT9LYMatn |
| Pipeline (Agents 1->2->3) | 02:00, 08:00, 14:00, 20:00 | find -> qualify (PS1 READY rows) -> breakdowns in analysis/ -> Agent 5 inbox | trig_01XE43zbBKzSyZ25q5t56a27 |
| Daily Brief (Agent 5) | 09:30 | briefs/YYYY-MM-DD.md + push notification | trig_017q1JFvfjby3VJ4tP6t8x3K |
| Weekly Report (Agent 5) | Thursday 19:00 | reports/YYYY-MM-DD-weekly.md, forecast, recommendations | trig_017EGQ2HahZLUXVQsW1BiKej |
Manage: https://claude.ai/code/routines . Old Drive-based routines (Daily Brief trig_01Wh4prEhuFQWuZpWVAMDgC6, Hourly Watcher trig_01Wa1oEe4KXVtjE8CfwffwRR, Prospecting trig_01DX26Fsp8obXD6wzN1A3HWy) stay disabled; safe to delete.
Verified 2026-11-24: Sales Desk run cloned the repo, read sheet/Gmail/Calendar/Fathom and pushed to main (commit bfe6e0d).

## Open issues
1. Cloud network still closed (test 2026-11-24 15:36 UTC: every site 000, WebFetch ENOTFOUND, Apify ERR_PROXY_TUNNEL). Pipeline works from WebSearch only until Mohamed opens the Default environment network.
2. Instagram needs a login; cloud can't read it.
3. Warm leads (Hussein, Mostafa, AbdulRahman D., Aser, Nermeen workshop 11-28): Agent 4 can't draft without the latest chat text. Mohamed pastes replies into the Message Queue Notes or state/decisions.md.
4. Routines use Mohamed's plan usage (a run on 2026-11-24 16:16 UTC hit the 5-hour limit). If limits bite, reduce Sales Desk frequency.
5. Local folder: always `git pull` before editing, the cloud pushes to main.
