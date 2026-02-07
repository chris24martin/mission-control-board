# Module 1 (Investing) — Trading Risk Policy + Approval Checklist

**Purpose:** This policy is the safety rail for *any* trading-related automation. Until you explicitly approve changes, the system stays **read-only / paper-only**.

## 0) Hard rule: default mode
- **Default:** read-only monitoring + journaling.
- **Paper trading:** allowed once this policy is accepted.
- **Live trading:** **disabled** until you explicitly approve enabling it (separate approval event).

## 1) Risk limits (hard constraints)
These are the “tripwires.” If any would be violated, the agent must *not* place/submit an order and must request approval (or refuse if it’s beyond limits).

### Position sizing
- **Max $ per new position:** ___ USD (fill in).
- **Max % of portfolio per position:** ___%.
- **Max total exposure (sum of positions opened by automation):** ___% of portfolio.

### Loss limits
- **Max loss per trade (planned risk):** ___% of position (or ___ USD).
- **Max daily loss (kill switch threshold):** ___ USD or ___% of portfolio.
- **Max weekly loss (kill switch threshold):** ___ USD or ___% of portfolio.

### Frequency limits
- **Max trades/day:** ___.
- **Max orders/hour:** ___.
- **No trading outside market hours** unless explicitly approved (and only for instruments where it’s valid).

### Instrument/strategy constraints
- Allowed instruments (pick one set):
  - [ ] ETFs only
  - [ ] Large-cap equities only
  - [ ] Options (only if you explicitly allow; defaults to **disallowed**)
  - [ ] Crypto (defaults to **disallowed**)
- Leverage/margin: **disallowed by default**.
- Shorts: **disallowed by default**.

## 2) Approval policy
### What requires explicit approval (always)
- Any **live order** submission.
- Any change to this policy.
- Any action involving **margin, leverage, shorting, options, or crypto**.
- Any trade that breaches *any* hard constraint above.

### Approval timeout + expiry
- Default approval expiry: **15 minutes** (configurable).
- If expired: agent **does not trade**, logs “approval expired,” and requests a fresh approval.

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
- order details (or “paper sim”) + outcome tracking
- approval record (message id / who approved / when)

**Storage location:** `mission-control-board/data/audit/m1_investing/YYYY-MM-DD/<trade_id>.json` (create if missing).

## 5) Paper-trading minimums (before any live enablement)
- Minimum paper period: **30 trading days** (or ___ trades) with weekly summaries.
- Track: win rate, avg win/loss, max drawdown, slippage assumptions, regime notes.

## 6) Kill switch behavior
If any kill threshold is hit:
- Immediately halt new trades.
- Send you a single high-signal DM with:
  - what threshold triggered
  - current exposure
  - proposed next actions
- Require explicit approval to resume.

## 7) Open questions to fill in (you decide)
1. Portfolio size basis for limits (broker equity vs cash vs total net worth?)
2. Max $/position and max %/position
3. Daily/weekly loss thresholds
4. Allowed instruments (ETFs only vs equities)
5. Paper-trading duration requirement (days vs # trades)

---

## Quick “minimum safe defaults” (if you want me to fill blanks temporarily)
If you say “use conservative defaults,” I will set:
- ETFs only, no margin/shorts/options/crypto
- Max $/position = **$500**
- Max %/position = **2%**
- Max daily loss = **$100**
- Max trades/day = **2**
- Paper period = **30 trading days**
