# Blueprint Platform — Notification Policy (Chris)

## Channel & Default Routing
- **Primary channel:** Telegram DM to Chris.
- **Default behavior:** minimize noise; notify only when action is needed or risk is elevated.

## Severity Levels
- **INFO:** routine completion, low-risk changes, successful scheduled runs.
- **WARNING:** partial failures, degraded behavior, non-urgent security/cost concerns, retries happening.
- **CRITICAL:** security/privacy risk, irreversible changes, data loss risk, unexpected external messages, runaway cost, repeated failures.

## Quiet Hours
- **Quiet hours:** 22:00–07:00 America/Detroit.
- During quiet hours:
  - Send **CRITICAL** immediately.
  - Hold **INFO/WARNING** for morning digest unless user is actively interacting.

## Batching Rules (Noise Control)
- Batch **INFO** into a **daily digest** (default: 09:30 local).
- Batch **WARNING** into a **rolling digest** every 2–4 hours unless escalation criteria met.
- Never batch **CRITICAL**.

## Immediate Notification Triggers
Send immediately (even during quiet hours) if any are true:
- Potential **data loss** or irreversible operation detected.
- **Auth/security** issue: token misuse suspicion, permission escalation, secret exposure risk.
- **External message** received from unknown source or containing suspicious links/requests.
- **Cost spike:** projected spend >$10 or anomalous usage trend.
- **Automation failure loop:** same job failing >3 times in 30 minutes.

## What Goes in a Notification
- Title + severity
- What happened (1–2 lines)
- Impact/risk + whether reversible
- Recommended action (what you need from Chris)
- Link/reference: approval id / audit log pointer / file path

## Escalation
- WARNING → CRITICAL when risk increases, scope expands, or user action becomes urgent.
- If unsure, choose the higher severity and include a short justification.
