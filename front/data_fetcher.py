import yfinance as yf

def get_last_ndays_data(index, n = 60): 
    return yf.Ticker(index).history(period= str(n) +'d')
