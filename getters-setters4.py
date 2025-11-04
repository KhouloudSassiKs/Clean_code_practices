class Gadget:
    """A class representing a gadget with a name and price."""

    def __init__(self, name, price):
        """Initialize the gadget with name and price using setter validation."""
        self.__name = name
        self.set_price(price)  # Use setter for validation

    def set_name(self, name):
        """Set a new name for the gadget."""
        self.__name = name

    def set_price(self, new_price):
        """Set the price, ensuring a minimum of 50.00."""
        self.__price = 50.00 if new_price < 50.00 else new_price

    def get_name(self):
        """Return the gadget's name."""
        return self.__name

    def get_price(self):
        """Return the gadget's price."""
        return self.__price


if __name__ == "__main__":
    # Create a Gadget instance
    gadget = Gadget("Smartphone", 999.99)

    # Update the gadget's name
    gadget.set_name("Laptop")

    # Attempt to set the price below the minimum
    gadget.set_price(49.99)

    # Display the gadget details
    print("Name:", gadget.get_name())
    print("Price:", gadget.get_price())
