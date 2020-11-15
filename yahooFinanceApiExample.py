import yfinance as yf

print("a")

msft = yf.Ticker("MSFT")

# get stock info
msft.info


# get historical market data, here max is 5 years.
msft.history(period="max")