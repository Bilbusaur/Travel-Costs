from utils.api_integration import get_distance, API_KEY

origin = "London, UK"
destination = "Manchester, UK"
distance = get_distance(API_KEY, origin, destination)

print(f"Distance from {origin} to {destination}: {distance} miles")
