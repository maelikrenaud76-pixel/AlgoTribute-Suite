import yfinance as yf
import pandas as pd

TICKER = "AAPL"

print("=== AlgoTribute — Fundamental Analyzer ===\n")
print(f"Loading fundamentals for {TICKER}...\n")

stock = yf.Ticker(TICKER)

info = stock.info

print("Company:", info.get("longName"))
print("Sector:", info.get("sector"))
print("Industry:", info.get("industry"))
print("\nKey Ratios:\n")

def show(label, key):
    print(f"{label:<20}: {info.get(key)}")

show("Market Cap", "marketCap")
show("P/E Ratio", "trailingPE")
show("Forward P/E", "forwardPE")
show("PEG Ratio", "pegRatio")
show("Return on Equity", "returnOnEquity")
show("Profit Margin", "profitMargins")
show("Debt-to-Equity", "debtToEquity")
show("Current Ratio", "currentRatio")
show("Quick Ratio", "quickRatio")

