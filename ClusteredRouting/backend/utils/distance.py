import math

# Function to calculate the Haversine distance between two coordinates (lat, lon)
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the Haversine distance between two points on the earth.
    Returns the distance in kilometers.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate distance
    distance = R * c
    return distance

# Example usage
if __name__ == "__main__":
    lat1, lon1 = 52.3791, 4.9014  # Example: Amsterdam coordinates
    lat2, lon2 = 48.8566, 2.3522  # Example: Paris coordinates
    distance = haversine(lat1, lon1, lat2, lon2)
    print(f"The distance between the two locations is: {distance} kilometers.")
