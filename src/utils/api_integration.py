import requests
API_KEY = "AIzaSyDMW-mucmUKwJ7EczKWAOW_uVqjyGtlsUo"

print("Requests version:", requests.__version__)

def get_distance(API_KEY, origin, destination):
    """
    Fetches the distance between two locations using Google Maps Distance Matrix API.
    """
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {
        "origins": origin,
        "destinations": destination,
        "key": API_KEY,
        "units": "imperial",  # Use "metric" for kilometers
        "mode": "driving",  # Ensure the calculation is for driving
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

       # Extract the distance
        distance_text = data["rows"][0]["elements"][0]["distance"]["text"]
        distance_value = float(distance_text.split()[0])  # Numeric value in miles
        

        return distance_value
        print("Full API Response:", data)  # Inside the get_distance function
    except (requests.RequestException, KeyError, IndexError, ValueError) as e:
        print(f"Error fetching distance: {e}")
        return None

