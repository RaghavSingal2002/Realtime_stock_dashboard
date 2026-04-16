from fastapi import FastAPI, HTTPException
from stock_utils import get_companies, get_data, get_summary, compare, predict_next_close
from data_loader import save_to_db, fetch_stock

app = FastAPI()



stocks = ["INFY.NS", "TCS.NS", "RELIANCE.NS"]

for stock in stocks:
    try:
        save_to_db(stock)
    except Exception as e:
        print(f"Error loading {stock}: {e}")



@app.get("/")
def home():
    return {"message": "Stock Data Intelligence API is running 🚀"}



@app.get("/companies")
def companies():
    return get_companies()



@app.get("/data/{symbol}")
def stock_data(symbol: str):
    try:
        df = get_data(symbol)
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@app.get("/summary/{symbol}")
def summary(symbol: str):
    try:
        return get_summary(symbol)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@app.get("/compare")
def compare_stocks(symbol1: str, symbol2: str):
    try:
        return compare(symbol1, symbol2)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@app.get("/predict/{symbol}")
def predict(symbol: str):
    try:
        df = fetch_stock(symbol)
        return {
            "symbol": symbol,
            "predicted_next_close": predict_next_close(df)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))