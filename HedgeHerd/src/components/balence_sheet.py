#!/usr/bin/env python
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import certifi
import json

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

def get_available_dates(symbol):
    base_url = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/"
    full_url = f"{base_url}{symbol}?period=annual&apikey=A1s9cT8mYQCD0ZDRyFRM3YOjiLiUILHP"
    
    try:
        data = get_jsonparsed_data(full_url)
        dates = [entry["date"] for entry in data]
        return dates, data
    except Exception as e:
        return [], f"Error fetching data: {str(e)}"

def find_balance_sheet_by_date(data, target_date):
    for entry in data:
        if entry["date"] == target_date:
            return entry
    return None

if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    dates, data = get_available_dates(symbol)

    if isinstance(data, str):  # If error string is returned
        print(data)
    elif not dates:
        print(f"No balance sheet data found for {symbol}.")
    else:
        print(f"Available dates for {symbol}:")
        for i, d in enumerate(dates):
            print(f"{i+1}. {d}")
        
        choice = input("Pick a date from the list above (enter date exactly as shown): ")
        result = find_balance_sheet_by_date(data, choice)

        if result:
            print(json.dumps(result, indent=4))
        else:
            print(f"No data found for {choice}. Please make sure you typed it exactly.")
