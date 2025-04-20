#!/usr/bin/env python
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import certifi
import json

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

def main():
    print("📈 Stock Income Statement Report Generator")

    symbol = input("Enter the stock symbol (e.g., AAPL, TSLA, MSFT): ").upper()
    period = "annual"

    # Validate period
    if period not in ["annual", "quarter"]:
        print("❌ Invalid period. Please enter 'annual' or 'quarter'.")
        return

    url = f"https://financialmodelingprep.com/api/v3/income-statement/{symbol}?period={period}&apikey=A1s9cT8mYQCD0ZDRyFRM3YOjiLiUILHP"

    try:
        data = get_jsonparsed_data(url)
        if not data:
            print(f"❌ No data found for {symbol}.")
            return

        latest = data[0]
        print(f"\n✅ {symbol} {period.capitalize()} Report ({latest['date']})")
        print(f"Revenue: ${latest['revenue']:,}")
        print(f"Net Income: ${latest['netIncome']:,}")
        print(f"EPS: ${latest['eps']}")
        print(f"Operating Income: ${latest['operatingIncome']:,}")
        print(f"Gross Profit: ${latest['grossProfit']:,}")
        print(f"R&D Expenses: ${latest['researchAndDevelopmentExpenses']:,}")
        print(f"Link to full filing: {latest['finalLink']}")
    except Exception as e:
        print(f"❌ Error retrieving data: {e}")

if __name__ == "__main__":
    main()
