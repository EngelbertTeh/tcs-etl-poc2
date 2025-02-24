import matplotlib.pyplot as plt
import io
import base64
from flask import render_template

def visualize_data(df):
    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Close"], marker="o", label="Close Price")
    plt.xlabel("Date")
    plt.ylabel("Closing Price ($)")
    plt.title("SCB Stock Price Trend")
    plt.legend()
    plt.xticks(rotation=45)
    
    # Save the plot as a PNG image to BytesIO
    image_io = io.BytesIO()
    plt.savefig(image_io, format='png', bbox_inches='tight')
    image_io.seek(0)  # Move to the beginning of the BytesIO buffer
    
    # Encode the image to base64
    dataurl = 'data:image/png;base64,' + base64.b64encode(image_io.getvalue()).decode('ascii')
    
    # Close the plot to free up memory
    plt.close()
    
    # Return the base64-encoded image to render in HTML template
    return render_template('index.html', image_data=dataurl)
