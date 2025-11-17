import numpy as np
import yfinance as yf
import pandas as pd

PORTFOLIO = {
    "AAPL": 0.25,
    "MSFT": 0.25,
    "NVDA": 0.25,
    "AMZN": 0.25
}

SHOCK = -0.15   # -15% market crash

print("=== AlgoTribute — Stress Test ===\n")

tickers = list(PORTFOLIO.keys())
weights = list(PORTFOLIO.values())

data = yf.download(tickers, period="1mo")["Close"].dropna()
latest = data.iloc[-1]

print("Simulating shock:", SHOCK * 100, "%\n")

new_prices = latest * (1 + SHOCK)
losses = (new_prices - latest) * weights

total_loss = sum(losses)

print("Asset impact:")
for t, old, new in zip(tickers, latest, new_prices):
    print(f"{t}:  {old:.2f} → {new:.2f}")

print(f"\nPortfolio loss: {total_loss:.2f} USD (relative)")
