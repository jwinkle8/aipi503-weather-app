import datetime as dt
import requests
import os
from dotenv import load_dotenv

from user_preferences import UserPreferences
from weather_helpers import wind_deg_to_direction, get_temp_unit

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"

def modify_user_preferences(prefs: UserPreferences):
    """Save the user's preferences (in a given session) for displaying weather information."""
    measurement_system_input = input("Enter desired measurement system (options are \"standard,\" \"metric,\" and \"imperial\"): ")
    verbose_input = input("Would you like to enable verbose output (y/n)? ")

    if verbose_input in ["y", "n"] and measurement_system_input in ["standard", "metric", "imperial"]:
        prefs.set_measurement_system(measurement_system_input)
        prefs.set_verbose(verbose_input=="y")
        print("Preferences saved!")
    else:
        print("One or more invalid inputs were entered; returning to menu with no changes to preferences")

def print_verbose_weather(data: dict, prefs: UserPreferences):
    """Print more detailed information from a successful weather request's reponse."""
    humidity = data["main"]["humidity"]
    print(f"    - The humidity is {humidity}%.")

    wind_speed = data["wind"]["speed"]
    wind_speed_unit = "miles/hour" if prefs.get_measurement_system() == "imperial" else "meters/second"
    wind_deg = data["wind"]["deg"]
    wind_direction = wind_deg_to_direction(wind_deg)
    print(f"    - Winds are {wind_speed} {wind_speed_unit} to the {wind_direction}.")

    feels_like = data["main"]["feels_like"]
    print(f"    - The feels like temp is {feels_like}.")

    low = data["main"]["temp_min"]
    high = data["main"]["temp_max"]
    temp_unit = get_temp_unit(prefs)
    print(f"    - Today's high is {high}°{temp_unit} and the low is {low}°{temp_unit}.")

    sunrise = dt.datetime.fromtimestamp(data["sys"]["sunrise"]).time()
    sunset = dt.datetime.fromtimestamp(data["sys"]["sunset"]).time()
    print(f"    - Sunrise is at {sunrise}. Sunset is at {sunset}.")

def get_weather(prefs: UserPreferences):
    """
    Fetch weather for the given city and print it nicely.

    Modifications to the default output are controlled through the argument prefs.
    """
    city = input("Enter a city to get the weather for: ")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": prefs.get_measurement_system()
    }
    
    response = requests.get(URL, params=params)
    data = response.json()

    if data["cod"] == "404":
        print("No weather found for the city requested. Did you misspell it?")
        return
    
    city_name = data["name"]
    temp = data["main"]["temp"]
    temp_unit = get_temp_unit(prefs)
    description = data["weather"][0]["description"]
    
    print(f"In {city_name}, it is {temp}°{temp_unit} with {description}.")

    if prefs.get_verbose():
        print_verbose_weather(data, prefs)
        

def main():
    """Define the primary control loop for the application."""

    prefs = UserPreferences()

    welcome_message = "Welcome to the Duke AIPI weather app!"

    print(welcome_message)
    print(len(welcome_message) * '-')

    while True:
        print()
        print("1. Get current weather")
        print("2. Set user preferences (measurement system, weather verbosity)")
        print("3. Quit")

        user_selection = input("Enter an option: ")

        if user_selection == "1":
            get_weather(prefs)
        elif user_selection == "2":
            modify_user_preferences(prefs)
        elif user_selection == "3":
            print("Goodbye!")
            exit()

main()