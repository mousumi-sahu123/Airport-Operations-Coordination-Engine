import requests

def get_live_weather(lat: float, lon: float):
    """
    Fetches real-time weather metrics using the free Open-Meteo API.
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,visibility"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        current = data.get("current", {})
        return {
            "temperature_c": current.get("temperature_2m", 25.0),
            "wind_speed_kmh": current.get("wind_speed_10m", 10.0),
            "visibility_km": current.get("visibility", 10000) / 1000,
            "status": "success"
        }
    except Exception as e:
        return {
            "error": str(e),
            "status": "fallback",
            "temperature_c": 25.0,
            "wind_speed_kmh": 10.0,
            "visibility_km": 10.0
        }

if __name__ == "__main__":
    test_weather = get_live_weather(28.6139, 77.2090)
    print("Weather Service Test Output:", test_weather)