import yfinance as yf
import pandas as pd
import numpy as np

TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "AMD", "NFLX", "INTC"]

print("=== AlgoTribute — Correlation Screener ===\n")
print("Downloading data...\n")

data = yf.download(TICKERS, period="1y")["Close"].dropna()

corr_matrix = data.corr()

pairs = []
for t1 in TICKERS:
    for t2 in TICKERS:
        if t1 < t2:
            c = corr_matrix.loc[t1, t2]
            pairs.append((t1, t2, c))

pairs_sorted = sorted(pairs, key=lambda x: abs(x[2]), reverse=True)

print("Top correlated pairs:\n")
for p in pairs_sorted[:10]:
    print(f"{p[0]} - {p[1]}  | corr = {p[2]:.4f}")
