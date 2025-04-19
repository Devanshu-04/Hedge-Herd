import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Constants
API_KEY = 'A1s9cT8mYQCD0ZDRyFRM3YOjiLiUILHP'
SYMBOL = 'AAPL'
FROM_DATE = '2000-01-01'
URL = f'https://financialmodelingprep.com/api/v3/historical-price-full/{SYMBOL}?from={FROM_DATE}&serietype=line&apikey={API_KEY}'

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
plt.figure(figsize=(12, 6))
plt.plot(dates, prices, label=f'{SYMBOL} Close Price', linewidth=1.5)
plt.title(f'{SYMBOL} Historical Close Prices (2000-Present)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()

# Format x-axis to only show 1 date label every 100 points
skip = max(len(dates) // 10, 1)
plt.xticks(dates[::skip], rotation=45)

# Optional: tighten layout to avoid cut-off labels
plt.tight_layout()
plt.show()