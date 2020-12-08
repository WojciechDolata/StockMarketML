import yfinance as yf

def get_last_year_data(index): 
    return yf.Ticker(index).history(period="1y")
