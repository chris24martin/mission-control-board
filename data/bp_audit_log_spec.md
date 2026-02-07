# Blueprint Platform — Audit Log Specification

## Purpose
Maintain an append-only, human-readable audit trail for a single-user AI assistant environment (Chris + agent). Focus: accountability, troubleshooting, and safe rollback.

## Events to Log (minimum set)
1. **Config changes**: OpenClaw settings, model routing, credentials references (never secrets), feature flags.
2. **External messages**: inbound/outbound (Telegram DM), webhooks, email relays (if any).
3. **File modifications**: create/edit/delete/rename within workspace and mission-control-board.
4. **Cron/scheduled tasks**: add/remove/enable/disable jobs; run results for scheduled jobs.
5. **Model switches**: alias/model change, reason, cost tier.
6. **Command execution**: `exec` calls that change state (installs, service restarts, network calls).
7. **Access/permission changes**: sudo usage, token scope changes, new integrations.

## Log Record Format
- **Storage format:** JSON Lines (`.jsonl`) for easy parsing + grepping.
- **Required fields:**
  - `ts` (ISO-8601 with timezone)
  - `actor` (e.g., `chris`, `agent:charles`, `system`)
  - `session` (optional id/label)
  - `action` (verb, e.g., `file.edit`, `config.set`, `message.send`)
  - `target` (path/url/config key/chat id)
  - `summary` (1–2 sentence human-readable)
  - `outcome` (`success` | `failure` | `partial` | `canceled`)
  - `risk` (`low` | `med` | `high`)
  - `reversible` (boolean)
  - `refs` (optional: approval id, ticket, commit hash)
- **Optional fields:** `before`/`after` (small diffs only), `error` (string), `duration_ms`, `cost_estimate_usd`.

## Examples
```json
{"ts":"2026-02-07T10:57:00-05:00","actor":"agent:charles","action":"file.write","target":"mission-control-board/data/bp_approval_template.md","summary":"Create approval template doc","outcome":"success","risk":"low","reversible":true}
```

## Retention Policy
- Keep **90 days** of detailed logs locally.
- Keep **1-year** monthly rollups (counts by action/outcome + notable incidents).
- Never log secrets (tokens, passwords, full message bodies with sensitive data). Redact or hash.

## Storage Location
- Primary: `~/.openclaw/workspace/mission-control-board/audit/audit.jsonl`
- Rollups: `~/.openclaw/workspace/mission-control-board/audit/rollups/YYYY-MM.jsonl`
- Backups: include in private git repo or encrypted backup (user-managed).

## Operational Notes
- Append-only; no in-place edits. Corrections are new records with `action: audit.correct`.
- If logging fails, **block high-risk actions** and notify Chris.
