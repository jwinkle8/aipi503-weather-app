# aipi503-weather-app
A small application that fetches the weather for one city at a time and report it to the CLI.

Optionally, configure your favorite measurement system and the level of detail with which the weather is reported.

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
5. Run the aipi503-weather-app CLI.
    ```
    python weather_app.py
    ```
