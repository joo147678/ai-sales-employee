# Dashboard protocol (Mohamed, 2026-11-27)

Mohamed follows everything and decides from the **Sales Desk dashboard**: https://claude.ai/artifact/XzXqpjGgx7bYMYSR3RM5JH
It reads and writes the Google Sheet "Prospects Database" (1QNvVMQB_6CfiPJluHBVw9pprwGA1laKwPYRsotJUVf8). Every agent keeps these tabs up to date, or the dashboard goes stale.

## Tabs the dashboard reads
- **Prospects** (A–AD, PLAYBOOK §2) and **Message Queue** (PLAYBOOK §16): as before.
- **Reports** (A–F): `Date | Type | Title | Target | Text | Link`. Append one row per report, never edit old rows (the dashboard shows the newest per type / per target).
  - `Brief`: Agent 5, every daily brief. Text = the full brief markdown. Link = its GitHub URL.
  - `Weekly`: Agent 5, the Thursday report (full text).
  - `Breakdown`: Agent 3, one row per breakdown written or updated. Target = the Prospects sheet row number. Text = the full breakdown markdown.
  - `Pains` / `PainsWeekly`: Agent 6, its daily / weekly report (full text).
  - `Alert`: any agent, one row per URGENT item (agents/5-head-of-sales.md item 4). Title = one short line. Target = the sheet row if a lead. Text = what happened + what Mohamed must do (+ the Call File for a booked call). The dashboard shows it until Mohamed clicks "handled".
  - Text must stay under 45,000 characters (cell limit); if longer, put a summary and rely on the Link.
- **Decisions** (A–G): `Timestamp | Type | Target | Decision | Note | Status | Processed At`. Written by Mohamed through the dashboard. **Status `New` = not processed yet.**

## Decisions the team must process (Sales Desk run = Agents 4+5, every run, first thing)
Read Decisions rows with Status `New`, act, then set that row's F = `Done` and G = Cairo timestamp (update_values on that row only).
- `Prospect` (Target = row; Decision APPROVED / REJECTED; Note = reason): the dashboard already wrote column I. For REJECTED: write V = Lost and AD = the reason, and add the reason to `analysis/learning.md` as a correction (Agent 3 learns from it). For APPROVED: the prospect is eligible for a first message (Agent 4).
- `Message` (Target = Queue ID; Sent / Edited & Sent / Skip): the dashboard already wrote the Queue status. Sync the Prospects row as PLAYBOOK §16 says (follow-ups day 3 and day 6), then write `synced` in Queue Notes.
- `Reply` (Target = row; Note = the prospect's reply as Mohamed pasted it): this IS a real reply. Set P = today, V = Replied, then Agent 4 drafts the next message per agents/4 (conversation method), Agent 5 QA, into the Queue. If the reply asks the price, wants a call or says "مهتم": also an Alert row + email.
- `Alert` (Target = `R<row>` of the Reports row; Handled): mark the matching line in state/alerts.md as handled.
- `Instruction` (free text): Agent 5 copies it into state/decisions.md with the date and follows it from now on; if it changes a rule, note which file needs the change.

## Email notifications to Mohamed
Mohamed asked for email notifications (2026-11-27). The ONLY email any agent may send is a notification **to Mohamed's own Gmail address** (the address of the connected Gmail account; it is also given in the routine prompt), with Gmail `send_message`. Never email a prospect or anyone else (prospect emails stay Gmail drafts).
- **URGENT** (Sales Desk, each new urgent item, once): subject `Sales URGENT: <short line>`; body: 3–5 lines in Egyptian Arabic: what happened, what to do, the dashboard link.
- **Daily brief** (09:30): subject `Sales brief <date>: <#1 action>`; body: the top 3 actions, counts (ready to send, waiting approval, overdue), the dashboard link.
- **Weekly** (Thursday): subject `Sales weekly <date>: <the most important number>`; body: 5 lines + the dashboard link.
- No emojis. Never put tokens, passwords or other secrets in an email.
- Push notifications stay as they are (PushNotification), the email is in addition.
