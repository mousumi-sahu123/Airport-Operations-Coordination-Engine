from weather_service import get_live_weather
from prediction_service import evaluate_flight_weather_risk
print("Testing Weather Service:")
weather = get_live_weather(23.0225, 72.5714)
print(weather)
print("\nTesting Prediction Service Risk Evaluation:")
risk = evaluate_flight_weather_risk(23.0225, 72.5714)
print(risk)