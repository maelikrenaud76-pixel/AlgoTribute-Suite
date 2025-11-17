import yfinance as yf
import numpy as np
import pandas as pd

TICKERS = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL"]

print("=== AlgoTribute — Portfolio Optimizer ===\n")
print("Downloading price data...")

data = yf.download(TICKERS, period="1y")["Close"].dropna()
returns = data.pct_change().dropna()

cov = returns.cov() * 252
means = returns.mean() * 252

def portfolio_perf(weights):
    r = np.dot(weights, means)
    v = np.dot(weights.T, np.dot(cov, weights))
    return r, v

best_sharpe = -999
best_w = None

for _ in range(20000):
    w = np.random.random(len(TICKERS))
    w /= np.sum(w)
    r, v = portfolio_perf(w)
    sharpe = r / np.sqrt(v)
    if sharpe > best_sharpe:
        best_sharpe = sharpe
        best_w = w

print("\nOptimal Portfolio:")
for i, t in enumerate(TICKERS):
    print(f"{t}: {best_w[i]*100:.2f}%")

print(f"\nExpected Return: {np.dot(best_w, means):.3f}")
print(f"Volatility: {np.sqrt(np.dot(best_w.T, np.dot(cov, best_w))):.3f}")
print(f"Sharpe Ratio: {best_sharpe:.3f}")
