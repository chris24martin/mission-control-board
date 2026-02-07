# Paper Trade Report Template

**Policy Alignment**: This document complies with `m1_001_trading_risk_policy.md`

## 1. Approval Card Fields

| Field | Content |
|-------|---------|
| Trader | [Full Name/ID] |
| Strategy | [Strategy Name & Version] |
| Timeframe | [Start Date] → [End Date] |
| Notional Limit | $[Amount] |
| Risk Factor | [Level 1-5] (per policy) |
| Approval Status | ☐ Pending  ☑️ Approved  ☐ Rejected |

## 2. Risk Limits Check

### 2.1 Policy Compliance

- [ ] Position size ≤ 5% portfolio value per asset
- [ ] Max volatility exposure: σ ≤ [Value] (annualized)
- [ ] Correlation matrix checked for >0.7 intra-portfolio assets
- [ ] Worst-case scenario loss < 2% of capital

### 2.2 Actuals vs Limits

| Metric | Limit | Actual | Delta |
|--------|-------|--------|------|
| Beta Exposure | ≤ 1.2 | [Value] | [Value] |
| Max Drawdown | < 8% | [Value] | [Value] |
| Sharpe Ratio | > 1.5 | [Value] | [Value] |

## 3. Execution Record

```json
{
  "proposed": {"timestamp": "", "quantity": , "price": },
  "executed": {"timestamp": "", "quantity": , "fill_price": , "fee": },
  "slippage": "%",
  "status": "filled/partial/cancelled"
}
```

## 4. Audit Fields

- **Initiated**: [ISO8601 timestamp]
- **Last Updated**: [ISO8601]
- **Version**: v[0.0.1] (semver)
- **Hash**: SHA256 of final parameters: `0x...`
- **Reviewer**: [Name/Signature]

## 5. Post-Mortem Template

### Outcomes

| KPI | Target | Actual |
|-----|--------|--------|
| Return | +15% | [Value] |
| Volatility | <20% | [Value] |
| Calmar Ratio | >2.5 | [Value] |

### Root Cause Analysis (if underperformance)

- [ ] Market regime shift (uncaptured)
- [ ] Implementation error
- [ ] Data leakage
- [ ] Overfitting evidence

### Action Items

1. [Specific improvement: e.g., "Add VIX skew correction"]
2. [Specific data enhancement]
3. [Process refinement]
```

## ...`, 