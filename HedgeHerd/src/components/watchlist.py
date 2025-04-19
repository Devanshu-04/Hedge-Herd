import requests
import matplotlib.pyplot as plt

# Constants
API_KEY = 'A1s9cT8mYQCD0ZDRyFRM3YOjiLiUILHP'
SYMBOL = 'AAPL'
URL = f'https://financialmodelingprep.com/api/v3/historical-price-full/{SYMBOL}?serietype=line&apikey={API_KEY}'

# Fetch data
response = requests.get(URL)
data = response.json()

# Parse and sort historical data
if 'historical' not in data:
    print("❌ Failed to fetch data.")
    exit()

historical = data['historical']
dates = [entry['date'] for entry in historical][::-1]  # Reverse to chronological order
prices = [entry['close'] for entry in historical][::-1]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(dates, prices, label=f'{SYMBOL} Close Price', linewidth=2)
plt.title(f'{SYMBOL} Historical Close Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.grid(True)

# Show the chart in a pop-up window
plt.show()
