# aipi503-weather-app
A small application that fetches the weather for one city at a time.

Optionally, configure your favorite measurement system and the level of detail with which the weather is reported.

## Note for instructors

This repository contains my solutions for both Week 5 Day 1 and Week 5 Day 2. The below table describes my solutions for specific challenges:

| Day | Solution file |
|-------|----------------|
| Day 1 | weather_app.py |
| Day 2 | streamlit_weather_app.py |

## Setup
1. Create a virtual environment.
2. Install project dependencies:
    ```
    python -m pip install -r requirements.txt
    ```
3. Obtain an [OpenWeather](https://openweathermap.org/guide#openweather_api_overview) API Key.
4. Paste the following line into a file named `.env`
    ```
    OPENWEATHER_API_KEY=<your_key_here>
    ```
5. If running the CLI app, run `weather_app.py`.
    ```
    python weather_app.py
    ```
    Otherwise, run the `streamlit` application:
    ```
    python -m streamlit run streamlit_weather_app.py
    ```
