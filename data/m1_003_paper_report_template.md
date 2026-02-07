# Module 1 (Investing) — Paper Trading Templates (Proposal • Execution • Weekly Summary)

These templates are **paper-only** and designed to align with:
- `data/m1_001_trading_risk_policy.md` (approvals + limits + audit trail)
- future automation that *suggests* trades but never executes live without explicit approval

> Copy/paste workflow:
> 1) Fill **Paper Trade Proposal** (pre-trade)
> 2) After “paper fill”, append **Execution Record**
> 3) End of week, append **Weekly Summary**

---

## A) Paper Trade Proposal (PRE-TRADE)

**Trade ID:** `PT-YYYYMMDD-###`

### 1) What (order details)
- Instrument / Ticker:
- Side: Buy / Sell
- Thesis type: Trend / Mean reversion / Event / Other
- Order type (paper): Market / Limit / Stop / Stop-limit
- Proposed entry:
- Proposed stop (if any):
- Proposed take-profit (if any):
- Time horizon: Intraday / Swing / Position

### 2) Why (rationale)
- Trigger / setup:
- Key levels (support/resistance):
- Confirmation signals:
- Invalidation (what proves this wrong):

### 3) Risk (must be explicit)
- Planned risk per share (entry − stop):
- Planned position size (shares):
- Planned max loss (USD):
- Planned max loss (% of position):
- Estimated slippage assumption:

### 4) Constraints check (policy compliance)
Fill this out with **YES/NO** and numbers.
- Allowed instrument class? (ETFs-only / equities allowed):
- No margin/leverage/shorts/options/crypto?:
- Max $ per new position respected?:
- Max % portfolio per position respected?:
- Max daily loss / weekly loss respected (if loss hit)?:
- Trades/day limit respected?:

### 5) Alternatives
- Do nothing because:
- Smaller size because:
- Wait for confirmation because:

### 6) Approval card (what would be sent for approval)
> Use this block verbatim if you want to request approval.

**APPROVAL REQUEST — PAPER TRADE (no live execution)**
- What: {ticker} {side} {qty} @ {entry} (paper)
- Why: {1–2 sentence rationale}
- Risk: max loss ~{USD}; stop {stop}; exposure after trade {…}
- Constraints: {bullet list of limits checked}
- Timeout: {e.g., 15 min}
- Links/notes: {source links or internal notes}

### 7) Audit fields (for traceability)
- Strategy name/version:
- Data sources used:
- Timestamp (UTC):
- Notes:

---

## B) Execution Record (POST-TRADE)

### 1) Paper fill details
- Filled entry price:
- Filled quantity:
- Filled timestamp (UTC):
- Stop/TP adjustments (if any):

### 2) Exit details (when closed)
- Exit price:
- Exit timestamp (UTC):
- Reason for exit: Stop / TP / Time stop / Manual thesis change

### 3) Outcome
- P/L (USD):
- P/L (%):
- Max adverse excursion (MAE):
- Max favorable excursion (MFE):
- Notes on slippage realism:

### 4) Post-mortem
- What went as expected:
- What surprised me:
- What I’d do differently next time:
- Was this trade consistent with policy? (Y/N + why)

---

## C) Weekly Summary (end-of-week)

**Week:** YYYY-MM-DD → YYYY-MM-DD

### 1) Snapshot
- # paper trades opened:
- # closed:
- Win rate:
- Avg win / Avg loss:
- Net P/L (paper, USD):
- Max drawdown (paper):

### 2) Regime notes
- Market regime (trend/range/volatile):
- Rates/vol notes:
- Key news/events:

### 3) Best + worst
- Best trade (why it worked):
- Worst trade (what failed):

### 4) Process quality (score 1–5)
- Setup quality:
- Risk discipline:
- Patience/overtrading:
- Documentation quality:

### 5) Next week adjustments
- Keep doing:
- Stop doing:
- Try:

---

## D) Filled Example (short)

### Paper Trade Proposal
- Trade ID: PT-20260207-001
- Instrument: SPY
- Side: Buy
- Order type: Limit
- Proposed entry: 500.00
- Proposed stop: 492.50
- Proposed take-profit: 512.00
- Horizon: Swing (3–10 days)

**Why:** Trend continuation after pullback to prior support; looking for reclaim of 20DMA with improving breadth.

**Risk:**
- Risk/share: 7.50
- Size: 10 shares
- Max loss: $75 (+ slippage)

**Constraints check:**
- Allowed instrument class: YES (ETF)
- No margin/shorts/options/crypto: YES
- Max $/position respected: YES (placeholder limit)
- Trades/day respected: YES

### Execution Record
- Filled entry: 500.10 @ 2026-02-07T15:10:00Z
- Exit: 511.80 @ 2026-02-12T19:45:00Z (TP)
- P/L: +$117 (paper)

**Post-mortem:** Entry was slightly late; stop was never threatened. Would scale out earlier next time.
