import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tickers = ["KO", "PEP"]
df = yf.download(tickers, period="6mo")["Close"].dropna()

spread = df["KO"] - df["PEP"]
spread_mean = spread.mean()
spread_std = spread.std()
z = (spread - spread_mean) / spread_std

long_signal = z < -2
short_signal = z > 2

position = pd.Series(index=df.index, dtype="object")
position[long_signal] = "long"
position[short_signal] = "short"
position = position.ffill().fillna("flat")

returns = df.pct_change().dropna()

pnl = pd.Series(0.0, index=returns.index)
pnl[position.shift(1) == "long"] = returns["KO"] - returns["PEP"]
pnl[position.shift(1) == "short"] = returns["PEP"] - returns["KO"]
pnl_cum = pnl.cumsum()

plt.figure(figsize=(12,5))
plt.plot(spread)
plt.axhline(spread_mean + 2*spread_std, color="red", linestyle="--")
plt.axhline(spread_mean - 2*spread_std, color="green", linestyle="--")
plt.title("Spread with Thresholds")
plt.show()

plt.figure(figsize=(12,5))
plt.plot(pnl_cum)
plt.title("Cumulative PnL")
plt.show()

print("Total Return:", pnl_cum.iloc[-1])
print("Win Rate:", (pnl > 0).mean())
print("Trades:", long_signal.sum() + short_signal.sum())





