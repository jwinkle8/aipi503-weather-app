from dotenv import load_dotenv
import datetime as dt
import os
import requests

from user_preferences import UserPreferences

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str, prefs: UserPreferences):
    """
    Get current weather for a given city str.
    
    Format data according to user preference.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": prefs.get_measurement_system()
    }
    
    data = requests.get(URL, params=params).json()

    if data["cod"] == "404":
        return None
    else:
        weather_data = {
            "city": data["name"],
            "temp": round(data["main"]["temp"]),
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "wind_speed_unit": "mi/hr" if prefs.get_measurement_system() == "imperial" else "m/s",
            "wind_direction" : _wind_deg_to_direction(data["wind"]["deg"]),
            "feels_like": round(data["main"]["feels_like"]),
            "low": round(data["main"]["temp_min"]),
            "high": round(data["main"]["temp_max"]),
            "temp_unit": _get_temp_unit(prefs),
            "sunrise": dt.datetime.fromtimestamp(data["sys"]["sunrise"]).time().strftime("%I:%M %p EST"),
            "sunset": dt.datetime.fromtimestamp(data["sys"]["sunset"]).time().strftime("%I:%M %p EST")
        }
        return weather_data

def describe_weather(city: str, prefs: UserPreferences):
    """
    Fetch weather for the given city and print it nicely.

    Modifications to the default output are controlled through the argument prefs.
    """
    data = get_weather(city, prefs)

    weather_str = "\n"
    if data is None:
        return weather_str + "No weather found for the city requested. Did you misspell it?"
    else:
        weather_str += f"In {data['city']}, it is {data['temp']}°{data['temp_unit']} with {data['description']}."

        if prefs.get_verbose():
            weather_str += ("\n" + f"""Here are some more deatils about today's weather:
    - The humidity is {data['humidity']}%.
    - Winds are {data['wind_speed']} {data['wind_speed_unit']} to the {data['wind_direction']}.
    - The feels like temp is {data['feels_like']}°{data['temp_unit']}.
    - Today's high is {data['high']}°{data['temp_unit']} and the low is {data['low']}°{data['temp_unit']}.
    - Sunrise is at {data['sunrise']} EST. Sunset is at {data['sunset']} EST.""")

        return weather_str

def _wind_deg_to_direction(wind_deg):
    """Convert a meteorological measure of the wind direction in degrees to a descriptive string."""
    if wind_deg >= 22.5 and wind_deg < 67.5:
        return "Northeast"
    elif wind_deg >= 67.5 and wind_deg < 112.5:
        return "East"
    elif wind_deg >= 112.5 and wind_deg < 157.5:
        return "Southeast"
    elif wind_deg >= 157.5 and wind_deg < 202.5:
        return "South"
    elif wind_deg >= 202.5 and wind_deg < 247.5:
        return "Southwest"
    elif wind_deg >= 247.5 and wind_deg < 292.5:
        return "West"
    elif wind_deg >= 292.5 and wind_deg < 337.5:
        return "Northwest"
    else:
        return "North"

def _get_temp_unit(prefs: UserPreferences):
    """Return the temperature unit for the user's preferred measurement system."""
    measurement_system = prefs.get_measurement_system()
    if measurement_system == "standard":
        return "K"
    elif measurement_system == "imperial":
        return "F"
    elif measurement_system == "metric":
        return "C"
