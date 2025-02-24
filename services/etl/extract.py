import yfinance as yf

# extract data
def extract_stock_data(ticker="SCBFF"):
  stock = yf.Ticker(ticker)
  df = stock.history(period="30d")
  return df
