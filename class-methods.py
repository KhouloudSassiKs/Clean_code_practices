"""
This code provides a Converter class for temperature and distance conversions.

Update note:
Refactored the code to extract common fixed values (conversion factors and offsets)
into class-level constants and implemented class methods to access them.
"""

class Converter:
    temp_factor = 9 / 5
    kilometer_factor = 0.621371
    offset = 32
    
    @classmethod
    def celsius_to_fahrenheit(cls, celsius):
        """Convert Celsius to Fahrenheit."""
        return celsius * cls.temp_factor + cls.offset
    
    @classmethod
    def fahrenheit_to_celsius(cls, fahrenheit):
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - cls.offset) / cls.temp_factor

    @classmethod
    def kilometers_to_miles(cls, kilometers):
        """Convert kilometers to miles."""
        return kilometers * cls.kilometer_factor

    @classmethod
    def miles_to_kilometers(cls, miles):
        """Convert miles to kilometers."""
        return miles / cls.kilometer_factor


def main():
    converter = Converter()
    
    temp_c = 25
    temp_f = converter.celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is {temp_f}°F")

    distance_km = 100
    distance_mi = converter.kilometers_to_miles(distance_km)
    print(f"{distance_km} km is {distance_mi} mi")


if __name__ == "__main__":
    main()
