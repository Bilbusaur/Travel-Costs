import requests
API_KEY = "AIzaSyDMW-mucmUKwJ7EczKWAOW_uVqjyGtlsUo"  # Replace with your actual API key

print("Requests version:", requests.__version__)

def get_distance_and_time(api_key, origin, destination):
    """
    Fetches the distance and travel time between two locations using Google Maps Distance Matrix API.

    Parameters:
        api_key (str): Google Maps API key.
        origin (str): Starting location.
        destination (str): Destination location.

    Returns:
        tuple: (distance in miles, travel time in minutes) or (None, None) if an error occurs.
    """
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    params = {
        "origins": origin,
        "destinations": destination,
        "key": api_key,
        "units": "imperial",  # Use "metric" for kilometers
        "mode": "driving",  # Ensure the calculation is for driving
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Extract the distance and travel time
        distance_text = data["rows"][0]["elements"][0]["distance"]["text"]
        distance_value = float(distance_text.split()[0])  # Numeric value in miles

        time_text = data["rows"][0]["elements"][0]["duration"]["text"]
        time_minutes = data["rows"][0]["elements"][0]["duration"]["value"] // 60  # Convert seconds to minutes

        return distance_value, time_minutes
    except (requests.RequestException, KeyError, IndexError, ValueError) as e:
        print(f"Error fetching distance or time: {e}")
        return None, None