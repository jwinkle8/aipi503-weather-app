from user_preferences import UserPreferences
from weather_helpers import describe_weather

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
            city = input("Enter a city to get the weather for: ")
            print(describe_weather(city, prefs))
        elif user_selection == "2":
            modify_user_preferences(prefs)
        elif user_selection == "3":
            print("Goodbye!")
            exit()

main()