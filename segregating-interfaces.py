# Demonstrating Interface Segregation Principle (ISP)
# Refactored a single Vehicle interface into three smaller, purpose-specific interfaces.

class Drive:
    """Interface for drivable vehicles."""
    def drive(self):
        pass


class OpenDoor:
    """Interface for vehicles with doors."""
    def open_door(self):
        pass


class Pedal:
    """Interface for vehicles that require pedaling."""
    def pedal(self):
        pass


class Car(Drive, OpenDoor):
    """Car implements driving and door-opening capabilities."""
    def drive(self):
        print("Car is driving")

    def open_door(self):
        print("Car door is opening")


class Bicycle(Pedal, Drive):
    """Bicycle implements pedaling and driving capabilities."""
    def pedal(self):
        print("Bicycle is pedaling")

    def drive(self):
        print("Bicycle is moving forward")


def main():
    car = Car()
    car.drive()
    car.open_door()

    bicycle = Bicycle()
    bicycle.pedal()
    bicycle.drive()


if __name__ == "__main__":
    main()
