import yfinance as yf
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def fetch_usdbrl_value():
    usdbrl = yf.Ticker("BRL=X")
    data = usdbrl.history(period="1d") # Fetch daily data
    lastest_close = round(data["Close"].iloc[-1], 2)
    return lastest_close