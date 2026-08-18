from user_preferences import UserPreferences

def wind_deg_to_direction(wind_deg):
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

def get_temp_unit(prefs: UserPreferences):
    """Return the temperature unit for the user's preferred measurement system."""
    measurement_system = prefs.get_measurement_system()
    if measurement_system == "standard":
        return "K"
    elif measurement_system == "imperial":
        return "F"
    elif measurement_system == "metric":
        return "C"