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
4. **Agent 4, Follow-up:** checks who booked a call from Agent 3's conversations; sends follow-ups to those who didn't reply. First follow-up 3–4 days after the first message. If the prospect replies, no follow-up: the conversation continues with the conversation agent.
   - Mohamed asked: if follow-up alone is too little for its own agent, merge it.

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
