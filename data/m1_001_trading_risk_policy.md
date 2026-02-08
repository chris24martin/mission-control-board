# Module 1 (Investing) — Trading Risk Policy + Approval Checklist

<!-- Conservative defaults applied by Charles — review and adjust. -->

**Purpose:** This policy is the safety rail for *any* trading-related automation. Until you explicitly approve changes, the system stays **read-only / paper-only**.

## 0) Hard rule: default mode
- **Default:** read-only monitoring + journaling.
- **Paper trading:** allowed once this policy is accepted.
- **Live trading:** **disabled** until you explicitly approve enabling it (separate approval event).

## 1) Risk limits (hard constraints)
These are the "tripwires." If any would be violated, the agent must *not* place/submit an order and must request approval (or refuse if it's beyond limits).

### Position sizing
- **Max $ per new position:** $5,000 USD (paper trades only).
- **Max % of portfolio per position:** 5%.
- **Max total exposure (sum of positions opened by automation):** 20% of portfolio.

### Loss limits
- **Max loss per trade (planned risk):** 5% of position (or $250 USD).
- **Max daily loss (kill switch threshold):** $500 USD or 2% of portfolio.
- **Max weekly loss (kill switch threshold):** $1,000 USD or 4% of portfolio.

### Frequency limits
- **Max trades/day:** 3.
- **Max orders/hour:** 5.
- **No trading outside market hours** unless explicitly approved (and only for instruments where it's valid).

### Instrument/strategy constraints
- Allowed instruments:
  - [x] ETFs only
  - [x] Large-cap equities only (NVDA, TSLA, ARM, etc.)
  - [ ] Options — **disallowed by default**
  - [ ] Crypto — **disallowed by default** (monitoring only via Coinbase; no automated trades)
- Leverage/margin: **disallowed by default**.
- Shorts: **disallowed by default**.

## 2) Approval policy
### What requires explicit approval (always)
- Any **live order** submission.
- Any change to this policy.
- Any action involving **margin, leverage, shorting, options, or crypto**.
- Any trade that breaches *any* hard constraint above.
- **All paper trades** during the 90-day evaluation period.

### Approval timeout + expiry
- Default approval expiry: **15 minutes** (configurable).
- If expired: agent **does not trade**, logs "approval expired," and requests a fresh approval.

### Paper-to-live transition requirements
- **Minimum paper-only period: 90 trading days** before any live consideration.
- Must demonstrate positive expectancy over the paper period.
- Explicit written approval required from Chris to enable live trading.

## 3) Approval card template (what you should see)
When asking you to approve a trade, the agent must include:
1. **What**: instrument, side (buy/sell), qty, order type, limit/stop prices
2. **Why**: signal/trigger + brief rationale
3. **Risk**: max loss estimate, stop/invalidations, exposure after trade
4. **Constraints check**: confirm each relevant limit is satisfied
5. **Alternatives**: do nothing / smaller size / wait for confirmation
6. **Links**: relevant chart/news/notes + internal analysis doc
7. **Timeout**: when approval expires
8. **Rollback**: how to exit/cancel if wrong

## 4) Audit trail (required)
Every proposed trade (paper or live) must be logged with:
- timestamp, strategy name/version, data sources
- inputs snapshot (signals/features used)
- decision + reasoning
- order details (or "paper sim") + outcome tracking
- approval record (message id / who approved / when)

**Storage location:** `mission-control-board/data/audit/m1_investing/YYYY-MM-DD/<trade_id>.json` (create if missing).

## 5) Paper-trading minimums (before any live enablement)
- Minimum paper period: **90 trading days** with weekly summaries.
- Track: win rate, avg win/loss, max drawdown, slippage assumptions, regime notes.
- Require Chris's explicit review and approval after paper period completes.

## 6) Kill switch behavior
If any kill threshold is hit:
- Immediately halt new trades.
- Send you a single high-signal DM with:
  - what threshold triggered
  - current exposure
  - proposed next actions
- Require explicit approval to resume.

## 7) Platforms and accounts (reference only)
- **Robinhood:** stocks/ETFs (NVDA, TSLA, ARM)
- **Coinbase:** crypto (BTC, ETH) — **monitoring only, no automated trades**

## 8) Conflict of interest note
Chris is VP/Senior Staff Engineer at Comerica Bank. Avoid trading $CMA or any directly related financial institution without explicit approval and compliance review.

---

## Quick reference: Conservative defaults (ACTIVE)
| Limit | Value |
|-------|-------|
| Max $/paper position | $5,000 |
| Max %/position | 5% |
| Max daily loss | $500 |
| Max weekly loss | $1,000 |
| Max trades/day | 3 |
| Paper period before live | 90 trading days |
| Approval required | ALL trades (paper and live) |
| Crypto trading | Monitoring only |
| Options/margin/shorts | Disallowed |
