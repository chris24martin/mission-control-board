# Blueprint Platform — Execution Pre-Flight Checklist

Use this checklist before any **significant** action (state changes, external calls, installs, deletions, config edits, automations).

## A) Safety Checks
- [ ] I understand the goal and the minimal action needed.
- [ ] I reviewed the exact commands/edits I will perform.
- [ ] No secrets will be printed, logged, or pasted into files.
- [ ] If touching security/privacy, I have explicit approval.

## B) Reversibility & Backups
- [ ] I can describe rollback steps in 1–5 commands.
- [ ] I identified the affected files/services and blast radius.
- [ ] Backup/snapshot created (or confirmed unnecessary).
- [ ] For deletions: I will prefer move-to-trash/archive over hard delete.

## C) Notification Requirements
- [ ] Severity assessed: info / warning / critical.
- [ ] Chris has been notified if required by policy (see `bp_notification_policy.md`).
- [ ] If during quiet hours, I will only interrupt for critical items.

## D) Cost & Time Implications
- [ ] Estimated cost tier: low (<$1) / medium ($1–$10) / high (>$10).
- [ ] Runtime expectation stated (seconds/minutes/hours) and any timeouts set.
- [ ] For high-cost actions, I have approval and a stopping condition.

## E) Permission Level
- [ ] No elevated permissions required, or:
- [ ] If sudo/elevated is needed: explicit confirmation obtained.
- [ ] External integrations (Telegram/web/API) authorized for this action.

## F) Execution Plan
- [ ] Dry-run/preview performed when possible.
- [ ] Steps ordered to minimize risk (read/inspect → small change → validate → larger change).
- [ ] Validation steps defined (tests, status checks, file diffs).
- [ ] Audit log entry will be recorded (action, target, outcome, rollback info).

## G) Post-Execution
- [ ] Validate success criteria.
- [ ] If failed/partial: rollback or contain blast radius.
- [ ] Summarize results + next steps for Chris (as required).
