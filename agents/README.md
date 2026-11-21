# The Sales Team: who does what, and how they work together

One team, one goal: turn Mohamed's ICP (CONTEXT.md §3) into Personal Brand clients.
Every agent reads, at the start of every run: `CONTEXT.md` → `VOICE.md` → `PLAYBOOK.md` → its own file in `agents/` → `state/team-board.md` → its inbox in `state/inbox/`.

## Org chart

```
                    Mohamed (approves prospects, every text, every price; sends; takes calls)
                                   ▲  urgent alerts + daily brief
                                   │
                  TL — Senior Sales Team Leader (orchestrates, QA gate, alerts)
     ┌──────────┬──────────┬───────┴───┬──────────┬──────────┬──────────┐
     P1         P2         S1          S2         S3         S4/S5      S6
  Lead Gen   Qualifier  Outreach   Follow-up  Reply &    Call Prep   Outcome &
  (24/7)     (24/7)     Planner               Qualify    & Proposal  Learning
                           └──────────┴─────┬────┴──────────┘
                                            W1 — Copywriter (writes every text in Mohamed's voice)
```

| Agent | File | Runs | Hands off to |
|---|---|---|---|
| TL Sales Team Leader | `TL-sales-team-leader.md` | Sat–Thu, every run of the team + 09:30 daily brief | everyone; Mohamed |
| P1 Lead Generator | `P1-lead-generator.md` | 24/7, every day incl. Friday | P2 |
| P2 Qualifier | `P2-qualifier.md` | 24/7, every day incl. Friday | TL → Mohamed (approval) → S1 |
| S1 Outreach Planner | `S1-outreach.md` | Sat–Thu | W1 → TL → Message Queue |
| S2 Follow-up | `S2-follow-up.md` | Sat–Thu | W1 → TL |
| S3 Reply & Qualify | `S3-reply-qualify.md` | Sat–Thu | W1 → TL; S4 when a call is booked |
| S4 Call Prep | `S4-call-prep.md` | Sat–Thu (and before any booked call) | S5 after the call |
| S5 Proposal & Close | `S5-proposal-close.md` | Sat–Thu | W1 → TL → Mohamed |
| S6 Outcome & Learning | `S6-outcome-learning.md` | Thursday weekly + on every Won/Lost | TL (updates library/learning-log) |
| W1 Copywriter | `W1-copywriter.md` | whenever an agent requests a text | TL (QA) |

## Working days
- **Friday is off for everything prospect-facing**: no drafts queued for Friday, no follow-up or reminder dates on a Friday, no brief. If a date lands on Friday, move it to Saturday.
- P1 and P2 run every day including Friday (they don't contact anyone).

## How agents talk to each other (the collaboration protocol)
1. **Team board** `state/team-board.md`: one row per active lead: stage, owner agent, last action, next action + date. The single picture everyone reads. Only the owner agent updates its row; TL can change any row.
2. **Inboxes** `state/inbox/<AGENT>.md`: a handoff is a line appended to the next agent's inbox:
   `YYYY-MM-DD HH:MM | from <AGENT> | lead <name> (sheet row N) | <what was done> | <what you need to do> | <links/evidence>`
   The receiving agent marks it `DONE <date>` when handled. Nothing is handed off verbally: if it's not in an inbox, it didn't happen.
3. **Run log** `state/run-log.md`: every agent appends one line per run (what it handled, counts, problems). TL reads it.
4. **Escalation** → `state/alerts.md` + urgent notification (TL file, "Alerts").
5. Every draft goes **W1 → TL QA → Message Queue**. No agent writes prospect-facing text itself; no draft reaches Mohamed without TL's QA.

## Source of truth
- Pipeline data: Google Sheet "Prospects Database" (PLAYBOOK §2).
- Rules and context: this repo / `D:\OUTREACH\ai-sales-employee`.
- Nothing is sent by any agent. Mohamed sends.

## Not built yet
- Reading WhatsApp / Instagram DM inboxes directly (Mohamed wants it later). Until then a reply exists only when Mohamed reports it (Decisions, sheet column M, or chat).
- Mohamed's outreach strategy: he will define it; it goes into PLAYBOOK §4 and the S1/S2 files.
