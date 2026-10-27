import pandas as pd
from weather_service import get_live_weather

def evaluate_flight_weather_risk(lat: float, lon: float):
    """
    Fetches real-time weather data and evaluates operational risks for flights.
    """
    weather = get_live_weather(lat, lon)
    
    wind_speed = weather.get("wind_speed_kmh", 0.0)
    visibility = weather.get("visibility_km", 10.0)
    temperature = weather.get("temperature_c", 25.0)
    
    risk_level = "Low"
    if wind_speed > 30.0 or visibility < 5.0:
        risk_level = "High"
    elif wind_speed > 20.0 or visibility < 8.0:
        risk_level = "Medium"
        
    return {
        "location": {"latitude": lat, "longitude": lon},
        "weather_data": {
            "temperature_c": temperature,
            "wind_speed_kmh": wind_speed,
            "visibility_km": visibility
        },
        "operational_risk": risk_level,
        "recommendation": "Normal operations" if risk_level == "Low" else "Caution: Weather delay advisory recommended"
    }

if __name__ == "__main__":
    # Test with sample airport coordinates (e.g., New Delhi Indira Gandhi International Airport)
    test_lat = 28.5562
    test_lon = 77.1000
    
    print("Running Weather & Prediction Service Test...")
    result = evaluate_flight_weather_risk(test_lat, test_lon)
    print("Result:", result)