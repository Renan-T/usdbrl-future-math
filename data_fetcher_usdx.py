import yfinance as yf
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def fetch_usdx_value():
    usdx = yf.Ticker("DX-Y.NYB")
    data = usdx.history(period="5d") #Fetch daily data and get friday data in mondays
    data = data.tail(2)

    latest_close = data["Close"].iloc[-1]
    previous_close = data["Close"].iloc[-2]

    percentual_variation = round((((latest_close - previous_close) / previous_close) * 100), 2)

    return percentual_variation