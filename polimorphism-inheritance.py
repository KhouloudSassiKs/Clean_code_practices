class Device:
    """Base class representing a generic device."""

    def __init__(self, name, power_status):
        """Initialize a device with a name and power status."""
        self.name = name
        self.power_status = power_status

    def status(self):
        """Display the device's name and power status."""
        print(f"Device: {self.name}, Power Status: {self.power_status}")


class Laptop(Device):
    """Represents a laptop, inherits from Device."""

    def __init__(self, name, power_status, os):
        """Initialize a laptop with name, power status, and operating system."""
        super().__init__(name, power_status)
        self.os = os

    def status(self):
        """Display the laptop's details including OS."""
        super().status()
        print(f"Operating System: {self.os}")


class Smartphone(Device):
    """Represents a smartphone, inherits from Device."""

    def __init__(self, name, power_status, carrier):
        """Initialize a smartphone with name, power status, and carrier."""
        super().__init__(name, power_status)
        self.carrier = carrier

    def status(self):
        """Display the smartphone's details including carrier."""
        super().status()
        print(f"Carrier: {self.carrier}")


def main():
    """Demonstrate inheritance and method overriding with Device subclasses."""
    laptop = Laptop("MacBook Pro", "On", "macOS")
    smartphone = Smartphone("iPhone", "Off", "Verizon")

    print("Laptop Status:")
    laptop.status()

    print("\nSmartphone Status:")
    smartphone.status()


if __name__ == "__main__":
    main()
