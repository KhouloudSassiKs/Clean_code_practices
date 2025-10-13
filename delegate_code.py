class User:
    """Represents a user who has an associated address."""
    def __init__(self, address):
        self._address = address

    def get_address(self):
        """Return the address object associated with the user."""
        return self._address

    def print_full_address(self):
        """Return the user's full formatted address."""
        return self._address.get_full_address()


class Address:
    """Represents a user's address, composed of a City and zip code."""
    def __init__(self, city, zip_code):
        self._city = city
        self._zip_code = zip_code

    def get_city(self):
        """Return the City object."""
        return self._city

    def get_zip_code(self):
        """Return the zip code."""
        return self._zip_code

    def get_full_address(self):
        """Return a formatted full address string."""
        return f"{self._city.get_city_name()}, {self._city.get_state()}, ZIP Code: {self._zip_code}"


class City:
    """Represents a city with its name and state."""
    def __init__(self, city_name, state):
        self._city_name = city_name
        self._state = state

    def get_city_name(self):
        """Return the name of the city."""
        return self._city_name

    def get_state(self):
        """Return the state of the city."""
        return self._state


if __name__ == "__main__":
    # Example usage
    user = User(Address(City("New York", "NY"), "10001"))
    full_address = user.print_full_address()
    print("Full Address:", full_address)
