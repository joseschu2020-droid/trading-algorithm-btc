import yfinance as yf

# 1. DESCARGA DATOS
btc = yf.download("BTC-USD", period="6mo", interval="1d")

# 2. MEDIAS MOVILES
btc["SMA20"] = btc["Close"].rolling(20).mean()
btc["SMA50"] = btc["Close"].rolling(50).mean()

# 3. SEÑALES
btc["signal"] = 0
btc.loc[btc["SMA20"] > btc["SMA50"], "signal"] = 1

btc["position"] = btc["signal"].diff()

# 4. FILTRAR SEÑALES
buy_signals = btc[btc["position"] == 1]
sell_signals = btc[btc["position"] == -1]

# 5. RESULTADOS SIMPLES
print("\nBUY SIGNALS:")
print(buy_signals[["Close"]])

print("\nSELL SIGNALS:")
print(sell_signals[["Close"]])
