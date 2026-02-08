# Module 1 (Investing) — Read-only Monitoring Scope + Data Sources

<!-- Conservative defaults applied by Charles — review and adjust. -->

## Goal
Set up **read-only** market monitoring that produces:
- daily snapshots
- a small number of high-signal alerts
- paper-trade "candidates" that always require approval (per `m1_001_trading_risk_policy.md`)

No brokerage connectivity or order submission in this phase.

---

## 1) What to monitor (active watchlist)

### A) Chris's holdings (primary focus)
| Ticker | Name | Platform | Type |
|--------|------|----------|------|
| NVDA | NVIDIA | Robinhood | Equity |
| TSLA | Tesla | Robinhood | Equity |
| ARM | ARM Holdings | Robinhood | Equity |
| BTC | Bitcoin | Coinbase | Crypto |
| ETH | Ethereum | Coinbase | Crypto |

### B) Interest list (metals)
| Ticker | Name | Type |
|--------|------|------|
| GLD | SPDR Gold Shares | ETF |
| GC | Gold Futures | Commodity |
| SLV | iShares Silver Trust | ETF |
| SI | Silver Futures | Commodity |

### C) Broad market regime
- US indices: **SPY (S&P 500)**, **QQQ (Nasdaq 100)**, **IWM (Russell 2000)**
- Volatility: **VIX** (CBOE Volatility Index)
- Dollar: **DXY** (US Dollar Index)
- Market breadth (optional): adv/decline, new highs/lows

### D) Rates + credit (macro)
- **10Y Treasury yield** (TNX or source series)
- **2Y yield**, **yield curve** (2s10s)
- **credit spreads** (if accessible)

### E) Inflation/real economy (calendar-driven)
- CPI, PPI, unemployment, FOMC dates, earnings season notes

### F) Sectors (optional, disabled by default)
- XLK, XLF, XLE, XLI, XLV

---

## 2) Cadence + outputs

### Daily (15–60 seconds read)
- **Schedule:** Every trading day, after market close (4:30 PM ET)
- Market snapshot (index % changes, key levels, notable movers)
- Holdings performance summary (NVDA, TSLA, ARM, BTC, ETH)
- 0–3 alerts only (see thresholds)

### Weekly (5–10 minutes read)
- **Schedule:** Sundays 8 PM ET
- Regime summary: trend/range, vol, rates direction
- Holdings weekly performance
- Metals update (GLD, SLV)
- "Top setups" list (paper-only)
- Risk recap: would any proposed setup violate policy limits?

---

## 3) Alerting policy (low noise)
Only alert on *rare/high-impact* events:
- Index move: SPY/QQQ **±2% intraday** or **±4% over 5 trading days**
- VIX spike: **+25% in 1 day** or VIX above **30**
- Holdings alert: NVDA, TSLA, or ARM moves **≥8% in a day** (or earnings gap)
- Crypto alert: BTC or ETH moves **≥10% in a day**
- Rates shock: 10Y yield change **≥ 15 bps/day**
- Metals move: GLD or SLV moves **≥5% in a day**

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

## 5) Deliverables
- `data/m1_watchlist.json` — populated with holdings + interests
- Daily/weekly report templates (see m1_003_paper_report_template.md)
- Lightweight signals spec (simple trend/vol triggers) suitable for paper ideas

---

## 6) Platform reference (no credentials stored)
| Platform | Use | Holdings |
|----------|-----|----------|
| Robinhood | Stocks/ETFs | NVDA, TSLA, ARM |
| Coinbase | Crypto | BTC, ETH |

---

## 7) Quick settings summary
| Setting | Value |
|---------|-------|
| Check cadence | Daily (after close) |
| Summary cadence | Weekly (Sunday 8 PM ET) |
| Holdings monitored | NVDA, TSLA, ARM, BTC, ETH |
| Interests monitored | GLD, GC, SLV, SI |
| Indices monitored | SPY, QQQ, IWM, VIX, DXY |
| Alert window | Market hours + after-hours for crypto |
| ETFs allowed for paper ideas | Yes |
| Individual equities | Yes (large-cap only) |
