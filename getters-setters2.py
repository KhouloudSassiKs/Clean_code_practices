class Length:
    """A class to represent length in centimeters and convert between cm and inches."""

    def __init__(self, cm=0):
        """Initialize the Length object with a default value in centimeters."""
        self.__cm = cm

    def set_cm(self, cm):
        """Set the length value in centimeters."""
        self.__cm = cm

    def get_cm(self):
        """Return the length value in centimeters."""
        return self.__cm

    def set_inch(self, inch):
        """Convert inches to centimeters and set the length value."""
        self.__cm = inch * 2.54

    def get_inch(self):
        """Return the length value converted from centimeters to inches."""
        return self.__cm / 2.54


if __name__ == "__main__":
    # Example usage
    length = Length()

    # Convert centimeters to inches
    cm_value = 10
    length.set_cm(cm_value)
    inch_value = length.get_inch()
    print(f"{cm_value} cm is {inch_value} inches.")

    # Convert inches to centimeters
    inch_value = 5
    length.set_inch(inch_value)
    cm_value = length.get_cm()
    print(f"{inch_value} inches is {cm_value} cm.")
