# 🚀 Stock Data Intelligence Dashboard

A mini financial analytics platform that fetches real-time stock data, processes key financial metrics, and exposes insights through REST APIs with an optional machine learning prediction feature.

---

## 🎯 Objective

This project demonstrates:
- Real-world financial data handling
- Backend API development using FastAPI
- Data analysis & feature engineering
- Basic ML integration for stock price prediction

---

## ✨ Features

✅ Fetch real-time stock data using yfinance  
✅ Data cleaning & preprocessing with Pandas  
✅ Feature engineering:
  - Daily Returns  
  - 7-day Moving Average  
  - 52-week High & Low  

✅ REST APIs using FastAPI  
✅ SQLite database integration  
✅ Stock comparison between companies  
✅ 📈 ML-based next-day price prediction (Linear Regression)  

---

## 📊 APIs Overview

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/companies` | GET | List of available stocks |
| `/data/{symbol}` | GET | Last 30 days stock data |
| `/summary/{symbol}` | GET | 52-week high, low, avg |
| `/compare` | GET | Compare two stocks |
| `/predict/{symbol}` | GET | Predict next closing price |

---

## 🧠 Machine Learning Feature

A simple Linear Regression model is used to:
- Learn trends from historical closing prices  
- Predict the next day's closing price  

This demonstrates how ML can be integrated into financial analytics pipelines.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI  
- **Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Data Source:** yfinance  
- **Database:** SQLite  
- **ML Model:** Scikit-learn (Linear Regression)  
- **Visualization (Optional):** Chart.js  

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
- **git clone <your-repo-link>

# Navigate to project
- **cd stock_dashboard

# Install dependencies
- **pip install -r requirements.txt

# Run server
- **uvicorn app:app --reload


🌐 Access API
- **Open Swagger UI:

http://127.0.0.1:8000/docs
📌 Example Usage
🔹 Get Stock Data
/data/INFY.NS

🔹 Compare Stocks
/compare?symbol1=INFY.NS&symbol2=TCS.NS

🔹 Predict Price
/predict/RELIANCE.NS

📈 Key Insights
- **Daily returns help analyze short-term performance
- **Moving averages highlight trends
- **Comparison API identifies better-performing stocks
The prediction feature demonstrates future trend estimation
🚀 Future Improvements
- **Advanced ML models (LSTM, ARIMA)
- **Real-time streaming data
- **Interactive frontend dashboard
- **Deployment on cloud (Render / AWS)
- **Caching & performance optimization

🎥 Demo
- **(Optional) Add a short demo video link here showcasing:

API usage
- **Output responses
- **Prediction feature
🏁 Conclusion
- **This project showcases a complete pipeline: Data → Processing → API → Insights → ML

It reflects strong fundamentals in:

- **Backend development
- **Data handling
- **Analytical thinking
- **Practical ML integration
