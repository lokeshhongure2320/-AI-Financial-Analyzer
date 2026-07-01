import yfinance as yf

def stock_summary(ticker="AAPL"):
    df = yf.Ticker(ticker).history(period="1y")

    trend = "uptrend" if df["Close"].iloc[-1] > df["Close"].iloc[0] else "downtrend"

    return f"{ticker} stock is in {trend}. Price: {df['Close'].iloc[-1]}"