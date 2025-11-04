# TODO: Define the Vehicle class with attributes make and year
class Vehicle:
    """A class representing a vehicle with make and year."""

    def __init__(self, make, year):
        """Initialize the Vehicle with make and year."""
        self.__make = make
        self.__year = year

    def display(self):
        """Display the vehicle's make and year."""
        print(f"Make: {self.__make}, Year: {self.__year}")


# TODO: Define the Car class that inherits from Vehicle with an additional attribute model
class Car(Vehicle):
    """A class representing a car, inherited from Vehicle, with an additional model attribute."""

    def __init__(self, make, year, model):
        """Initialize the Car with make, year, and model."""
        super().__init__(make, year)
        self.model = model

    def display(self):
        """Display the car's make, year, and model."""
        super().display()
        print(f"Model: {self.model}")


if __name__ == "__main__":
    # TODO: Create an object of Car and call the display method to show its details
    my_car = Car("Tesla", 2026, "Model S")
    my_car.display()
