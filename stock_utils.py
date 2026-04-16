import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression



def get_companies():
    return ["INFY.NS", "TCS.NS", "RELIANCE.NS"]



def get_data(symbol):
    conn = sqlite3.connect("stocks.db")
    df = pd.read_sql(f"SELECT * FROM '{symbol}'", conn)
    conn.close()

    if df.empty:
        raise ValueError(f"No data found for {symbol}")

    return df.tail(30)



def get_summary(symbol):
    conn = sqlite3.connect("stocks.db")
    df = pd.read_sql(f"SELECT * FROM '{symbol}'", conn)
    conn.close()

    if df.empty:
        raise ValueError(f"No data found for {symbol}")

    if "Close" not in df.columns:
        raise ValueError(f"'Close' column missing in {symbol}")

    return {
        "52_week_high": float(df["Close"].max()),
        "52_week_low": float(df["Close"].min()),
        "average_close": float(df["Close"].mean())
    }



def compare(symbol1, symbol2):
    df1 = get_data(symbol1)
    df2 = get_data(symbol2)

    return {
        "symbol1_return": float(df1["Close"].pct_change().sum()),
        "symbol2_return": float(df2["Close"].pct_change().sum())
    }


def predict_next_close(df):
    # Use only Close column to avoid NaN issues
    df = df[['Close']].dropna()

    if len(df) < 2:
        raise ValueError("Not enough data for prediction")

    X = np.arange(len(df)).reshape(-1, 1)
    y = df['Close'].values

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[len(df)]])

    return float(prediction[0])