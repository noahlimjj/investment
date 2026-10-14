# Orchestrator notes: BABA (2026-10-13)
- **Share count:** sec_facts.py's shares_outstanding (1,858,037,427) is 1/10 of the true ordinary count, so don't use it. Use 18.58bn ordinary (31 Mar) or 19.90bn issued (29 Sep, after the Aug placing). 1 ADS = 8 ordinary shares; show the per-ADS conversion.
- **Earnings quality:** FY26 net income includes ~RMB 74bn of investment gains, so owner earnings from NI are unreliable. Build from operating income/EBITA plus a separate investment-book line (equity-method RMB 203bn, other stakes ~RMB 254bn at book, which needs a stated haircut).
- D&A is unresolved (XBRL 34,963 vs yfinance 47,118); state your choice. TTM capex is RMB 155bn (not the FY26 127bn): AI/cloud capex is surging and company FCF was −RMB 44.7bn in the June quarter.
- Vendor EV and EV/EBITDA are currency-mixed and invalid.
- **CNY 10y:** 1.67% (ChinaBond 2026-10-13, [FETCH]). Because BABA's ADS is priced in USD with a VIE/geopolitical overlay, decide the discount-rate currency explicitly. Don't pair a 1.67% CNY rate with USD cash flows.
- The orchestrator's own check confirms the tape: −33.6% over 12m (166.81 → 110.85 raw close), 52w low 94.81 (2026-06-26).
