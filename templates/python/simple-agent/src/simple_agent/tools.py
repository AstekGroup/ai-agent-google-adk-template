"""Outils pour l'agent simple."""

from google.adk.tools import FunctionTool
from typing import Literal
import os


def get_weather(
    city: str,
    units: Literal["celsius", "fahrenheit"] = "celsius"
) -> dict:
    """
    Get current weather information for a city.
    
    This is a mock implementation. Replace with actual API call to a weather service.
    
    Args:
        city: The name of the city
        units: Temperature units (celsius or fahrenheit)
    
    Returns:
        Dictionary containing weather information with keys:
        - status: "success" or "error"
        - city: City name
        - temperature: Temperature value
        - units: Temperature units
        - condition: Weather condition (e.g., "sunny", "rainy")
        - message: Error message if status is "error"
    """
    # Mock implementation - replace with real API call
    # Example: OpenWeatherMap, WeatherAPI, etc.
    
    # Mock data for demonstration
    mock_data = {
        "paris": {"temp": 15, "condition": "cloudy"},
        "london": {"temp": 12, "condition": "rainy"},
        "new york": {"temp": 20, "condition": "sunny"},
        "tokyo": {"temp": 18, "condition": "partly cloudy"},
    }
    
    city_lower = city.lower()
    
    if city_lower in mock_data:
        data = mock_data[city_lower]
        
        # Convert temperature if needed
        temp = data["temp"]
        if units == "fahrenheit":
            temp = (temp * 9/5) + 32
        
        return {
            "status": "success",
            "city": city,
            "temperature": str(temp),
            "units": units,
            "condition": data["condition"]
        }
    else:
        return {
            "status": "error",
            "city": city,
            "message": f"Weather information not available for {city}"
        }


# Créer l'outil ADK
get_weather_tool = FunctionTool(get_weather)
