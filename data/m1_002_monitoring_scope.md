# Module 1 (Investing) — Read-only Monitoring Scope + Data Sources

## Goal
Set up **read-only** market monitoring that produces:
- daily/weekly snapshots
- a small number of high-signal alerts
- paper-trade “candidates” that always require approval (per `m1_001_trading_risk_policy.md`)

No brokerage connectivity or order submission in this phase.

---

## 1) What to monitor (v1 watchlist)
### A) Broad market regime
- US indices: **SPY (S&P 500)**, **QQQ (Nasdaq 100)**, **IWM (Russell 2000)**
- Volatility: **VIX** (or VXX/vol proxies if needed)
- Market breadth (optional): adv/decline, new highs/lows

### B) Rates + credit (macro)
- **10Y Treasury yield** (TNX or source series)
- **2Y yield**, **yield curve** (2s10s)
- **credit spreads** (if accessible)

### C) Inflation/real economy (calendar-driven)
- CPI, PPI, unemployment, FOMC dates, earnings season notes

### D) Sector + themes (optional)
- XLK, XLF, XLE, XLI, XLV

### E) Personal “interest list” (you provide)
- 10–30 tickers you care about (companies/ETFs). This becomes the “candidate universe” for paper ideas.

---

## 2) Cadence + outputs
### Daily (15–60 seconds read)
- Market snapshot (index % changes, key levels, notable movers)
- 0–3 alerts only (see thresholds)

### Weekly (5–10 minutes read)
- Regime summary: trend/range, vol, rates direction
- “Top setups” list (paper-only)
- Risk recap: would any proposed setup violate policy limits?

---

## 3) Alerting policy (low noise)
Only alert on *rare/high-impact* events:
- Index move: SPY/QQQ **±2% intraday** or **±4% over 5 trading days**
- VIX spike: **+25% in 1 day** or VIX above a user-defined level
- Rates shock: 10Y yield change **≥ 15 bps/day**
- Portfolio-impacting: a watchlist name moves **≥ 8% in a day** (or earnings gap)

If multiple triggers happen in one session, collapse into **one** message.

---

## 4) Allowed data sources (v1)
**Preference order (lowest friction → more robust):**
1. **Public web sources** (read-only): exchange/finance sites, news releases (no scraping that violates ToS).
2. **CSV/manual inputs** from you (broker statements, watchlists).
3. Later (with explicit approval): a dedicated market data API.

### Explicitly disallowed in v1
- Any brokerage API keys/secrets stored by the agent without your explicit approval.
- Any automatic order routing/execution.

---

## 5) Deliverables (what I will generate once you confirm the scope)
- `data/m1_watchlist.json` template (tickers + categories)
- A daily/weekly report template
- A lightweight “signals” spec (simple trend/vol triggers) suitable for paper ideas

---

## 6) Questions for you (so I can finalize)
1. What broker/platform do you use (just name it — no credentials)?
2. Do you want **ETFs only** for paper ideas, or are individual equities OK?
3. Provide 10–30 tickers/ETFs you want on the interest list.
4. Preferred alert window: only market hours, or after-hours too?
