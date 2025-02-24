import matplotlib.pyplot as plt
import io
import base64

def visualize_data(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Close"], marker="o", label="Close Price")
    plt.xlabel("Date")
    plt.ylabel("Closing Price ($)")
    plt.title("Stock Price Trend")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

   

