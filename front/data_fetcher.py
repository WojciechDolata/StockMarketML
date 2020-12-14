import yfinance as yf

def get_last_60d_data(index): 
    return yf.Ticker(index).history(period="60d")

def get_last_30d_data(index): 
    return yf.Ticker(index).history(period="30d")
