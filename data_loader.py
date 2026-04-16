import yfinance as yf
import pandas as pd
import sqlite3

def fetch_stock(symbol):
    df = yf.download(symbol, period="1y", interval="1d")

    if df.empty:
        raise ValueError(f"No data fetched for {symbol}")

    df.reset_index(inplace=True)

   
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    print(f"{symbol} columns:", df.columns)

    
    if "Close" not in df.columns or "Open" not in df.columns:
        raise ValueError(f"Required columns missing: {df.columns}")

    df.dropna(inplace=True)

    
    df['Daily Return'] = (df['Close'] - df['Open']) / df['Open']
    df['7DMA'] = df['Close'].rolling(window=7).mean()
    df['52W High'] = df['Close'].rolling(window=252).max()
    df['52W Low'] = df['Close'].rolling(window=252).min()

    return df


def save_to_db(symbol):
    df = fetch_stock(symbol)

    conn = sqlite3.connect("stocks.db")
    df.to_sql(symbol, conn, if_exists='replace', index=False)
    conn.close()

    print(f"✅ Data saved for {symbol}")