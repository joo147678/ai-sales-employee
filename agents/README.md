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
     (24/7)          (24/7)     (breakdown with     (first message with the free value,
                                 Mohamed's thinking)  chat, follow-ups, call invite)
```

| Agent | File | Runs | Hands off to |
|---|---|---|---|
| 1 Prospect Finder | `1-prospect-finder.md` | 24/7, every day incl. Friday | Agent 2 |
| 2 Qualifier | `2-qualifier.md` | 24/7, every day incl. Friday | Agent 3 |
| 3 Account Analyst | `3-account-analyst.md` | every day (no prospect contact) | Agent 5 → Mohamed (approval) → Agent 4 |
| 4 Conversation Agent | `4-conversation-agent.md` | Sat–Thu | Agent 5 (QA) → Message Queue → Mohamed sends; Agent 5 when a call is booked |
| 5 Head of Sales | `5-head-of-sales.md` | every team run + 09:30 daily brief + Thursday weekly report | everyone; Mohamed |

Old team (TL, P1, P2, W1, S1–S6) is in `archive/agents-v1/` for reference only.

## Working days
- **Friday is off for everything prospect-facing**: no drafts for Friday, no follow-up dates on a Friday (move to Saturday), no brief.
- Agents 1, 2 and 3 run every day including Friday (they don't contact anyone).

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

## Still open (Mohamed will define)
- Agent 3's analysis method (Mohamed will send his past breakdowns to train it).
- Agent 4's message method after the first reply.
- Number and spacing of follow-ups after the first one.
- Where the agents run and how Mohamed approves and sends.
- Reading WhatsApp / Instagram inboxes directly (later). Until then a reply exists only when Mohamed reports it.
