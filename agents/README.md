# The Sales Team: 5 agents (Mohamed, 2026-11-24)

One team, one goal: turn Mohamed's ICP (CONTEXT.md §3) into clients on the right step of his offer ladder (CONTEXT.md §4).
Every agent reads, at the start of every run: `CONTEXT.md` → `VOICE.md` → `PLAYBOOK.md` → its own file in `agents/` → `state/team-board.md` → its inbox in `state/inbox/`.

## Org chart

```
              Mohamed (approves prospects, every text, every price; sends; takes calls)
                         ▲  urgent alerts · daily brief · weekly report + recommendations
                         │
              Agent 5 — Head of Sales (supervises the process, QA, alerts, reports, forecasts)
        ┌─────────────┬──┴──────────┬─────────────────┐
     Agent 1        Agent 2        Agent 3           Agent 4
  Prospect Finder → Qualifier → Account Analyst → Conversation Agent
     (24/6)          (24/6)     (breakdown with     (first message with the free value,
                                 Mohamed's thinking)  chat, follow-ups, call invite)
```

| Agent | File | Runs | Hands off to |
|---|---|---|---|
| 1 Prospect Finder | `1-prospect-finder.md` | 24/6 (Sat–Thu) | Agent 2 |
| 2 Qualifier | `2-qualifier.md` | 24/6 (Sat–Thu) | Agent 3 |
| 3 Account Analyst | `3-account-analyst.md` | 24/6 (Sat–Thu) | Agent 5 → Mohamed (approval) → Agent 4 |
| 4 Conversation Agent | `4-conversation-agent.md` | 24/6 (Sat–Thu) | Agent 5 (QA) → Message Queue → Mohamed sends; Agent 5 when a call is booked |
| 6 Audience Researcher | `6-audience-researcher.md` | Sat–Thu on Mohamed's laptop (Chrome: Reddit, FB groups, IG, LinkedIn) | Agent 1 (leads), Mohamed (pains report, comment drafts) |
| 5 Head of Sales | `5-head-of-sales.md` | every team run + 09:30 daily brief + Thursday weekly report | everyone; Mohamed |

Old team (TL, P1, P2, W1, S1–S6) is in `archive/agents-v1/` for reference only.

## Agent 6 (Mohamed, 2026-11-25)
Agent 6 listens to the audience on Reddit / Facebook groups / Instagram comments / LinkedIn, reports their problems and how they think (`research/pains/`), hands ICP people to Agent 1 and drafts helpful comments for Mohamed to post. Read only.

## Working days (Mohamed, 2026-11-24)
- The system runs in the **cloud, 24/6: Saturday to Thursday. Friday is off for every agent.** No drafts, no runs, no dates on Friday (move to Saturday).

## How agents talk to each other
1. **Team board** `state/team-board.md`: one row per active lead: stage, owner agent, last action, next action + date. Only the owner updates its row; Agent 5 can change any row.
2. **Inboxes** `state/inbox/<agent>.md`: a handoff is a line appended to the next agent's inbox:
   `YYYY-MM-DD HH:MM | from <agent> | lead <name> (sheet row N) | <what was done> | <what you need to do> | <links/evidence>`
   The receiving agent marks it `DONE <date>` when handled. If it's not in an inbox, it didn't happen.
3. **Run log** `state/run-log.md`: every agent appends one line per run.
4. **Alerts** `state/alerts.md` + urgent notification (Agent 5 file).
5. Every draft goes **Agent 4 → Agent 5 QA → Message Queue**. No draft reaches Mohamed without QA.

## Source of truth
- Pipeline data: Google Sheet "Prospects Database" (PLAYBOOK §2).
- Rules and context: this folder `D:\ai sales employee` + GitHub `joo147678/ai-sales-employee`.
- Nothing is sent by any agent. Mohamed sends.

## Still open
- Agent 3's analysis gets sharper as Mohamed corrects breakdowns (`analysis/learning.md`).
- Reading WhatsApp / Instagram inboxes directly (later). Until then a reply exists only when Mohamed reports it.
