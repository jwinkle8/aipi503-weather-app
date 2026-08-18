class UserPreferences:
    """Encapsulates the user's preferences for measurement system and verbosity of weather report."""

    def __init__(self, measurement_system: str = "metric", verbose: bool = False):
        """
        Create a default UserPreferences object.
        
        By default, set the measurement system to metric and verbosity off.
        """
        self.measurement_system = measurement_system
        self.verbose = verbose

    def set_measurement_system(self, measurement_system: str):
        self.measurement_system = measurement_system

    def get_measurement_system(self):
        return self.measurement_system

    def set_verbose(self, verbose: str):
        self.verbose = verbose

    def get_verbose(self):
        return self.verbose