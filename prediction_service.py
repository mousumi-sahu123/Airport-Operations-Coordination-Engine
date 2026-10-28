from weather_service import get_live_weather

def evaluate_flight_weather_risk(lat: float, lon: float):
    """
    Fetches real-time weather data and evaluates operational risks for flights.
    """
    # Fetch live weather from your weather service module[span_2](start_span)[span_2](end_span)
    weather = get_live_weather(lat, lon)
    
    # Extract weather parameters safely with default fallbacks[span_3](start_span)[span_3](end_span)
    wind_speed = weather.get("wind_speed_kmh", 0.0)
    visibility = weather.get("visibility_km", 10.0)
    temperature = weather.get("temperature_c", 25.0)
    
    # Risk evaluation logic based on meteorological conditions[span_4](start_span)[span_4](end_span)
    risk_level = "Low"
    if wind_speed > 30.0 or visibility < 5.0:
        risk_level = "High"
        
    return {
        "latitude": lat,
        "longitude": lon,
        "wind_speed_kmh": wind_speed,
        "visibility_km": visibility,
        "temperature_c": temperature,
        "risk_level": risk_level
    }

if __name__ == "__main__":
    print("Testing Prediction Service Risk Evaluation...")
    # Test using sample coordinates (e.g., Ahmedabad/Airport coordinates)
    sample_lat, sample_lon = 23.0225, 72.5714
    result = evaluate_flight_weather_risk(sample_lat, sample_lon)
    print("Prediction Result:", result)