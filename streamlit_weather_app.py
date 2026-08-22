import streamlit as st

from user_preferences import UserPreferences
from weather_helpers import get_weather

st.title("Streamlit Weather Web App")

# Collect user preferences
st.sidebar.title("User Preferences")
measurement_system = st.sidebar.radio(
    "Measurement system:",
    ["Imperial", "Metric", "Standard"],
    key="measurement_system"
)
verbose = st.sidebar.checkbox("Detailed weather", key="verbose")
prefs = UserPreferences(measurement_system.lower(), verbose)

# Collect user input city
city = st.text_input("Enter a city to get the weather for: ")

# Retreive requested weather data
weather_data = None
if city is not None and city != "":
    weather_data = get_weather(city, prefs)

# Display retreived data
if weather_data is not None:

    # Display simple temperature reading
    weather_dashboard_row1_col1, weather_dashboard_row1_col2, weather_dashboard_row1_col3 = st.columns(3)
    with weather_dashboard_row1_col1:
        st.metric(label="Temperature", value=f"{weather_data['temp']} °{weather_data['temp_unit']}")

    # Verbose weather reporting
    if prefs.get_verbose():

        with weather_dashboard_row1_col2:
            st.metric(label="Feels like", value=f"{weather_data['feels_like']} °{weather_data['temp_unit']}")
        with weather_dashboard_row1_col3:
            st.metric(label="Humidity", value=f"{weather_data['humidity']}%")

        weather_dashboard_row2_col1, weather_dashboard_row2_col2, weather_dashboard_row2_col3 = st.columns(3)
        with weather_dashboard_row1_col1:
            st.metric(label="Sunrise", value=f"{weather_data['sunrise']}")
        with weather_dashboard_row1_col2:
            st.metric(label="Sunset", value=f"{weather_data['sunset']}")
        with weather_dashboard_row1_col3:
            st.metric(label="Wind", value=f"{weather_data['wind_speed']} {weather_data['wind_speed_unit']}")