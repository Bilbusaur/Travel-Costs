import requests
#https://www.gov.uk/guidance/access-fuel-price-data
API_KEY = "your_fuel_api_key"  # Replace with your actual API key

def fetch_fuel_data(url):
    """
    Fetches fuel price data from the given URL.
    
    Parameters:
        url (str): The URL of the retailer's fuel price feed.
    
    Returns:
        dict or None: Parsed JSON data or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Parse JSON response
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def parse_diesel_price(data):
    """
    Parses fuel price data to calculate the average diesel price (B7).

    Parameters:
        data (dict): The JSON data from the API.
    
    Returns:
        float: The average price for B7 diesel, or None if no data is available.
    """
    try:
        stations = data["stations"]
        #extract B7 (diesel) prices
        prices_per_liter = [station["prices"]["B7"] / 100 for station in stations if "B7" in station["prices"]]

        if prices_per_liter:
            avg_price_per_liter = sum(prices_per_liter) / len(prices_per_liter)
            avg_price_per_gallon = avg_price_per_liter * 4.54609
            return avg_price_per_liter
        
        else:
            print("No B7 prices available")
            return None
    except KeyError as e:
        print(f"KeyError while parsing data: {e}")
        return None

"""    
if __name__ == "__main__":
    
    url = "https://jetlocal.co.uk/fuel_prices_data.json"
    fuel_data = fetch_fuel_data(url)
    if fuel_data:
        # Calculate average diesel price
        diesel_price = parse_diesel_price(fuel_data)
        if diesel_price is not None:
            print(f"Average diesel price (B7): £{diesel_price:.2f}")
        else:
            print("No diesel price data available.")
    else:
        print("Failed to fetch fuel data.")
"""

  
