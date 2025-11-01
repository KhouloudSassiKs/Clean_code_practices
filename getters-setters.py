class Person:
    """A class that demonstrates encapsulation using private attributes."""

    def __init__(self, name, age):
        # Private attributes (name mangling with double underscores)
        self.__name = name
        self.__age = age

    # Setter methods
    def set_name(self, new_name):
        """Set a new value for name."""
        self.__name = new_name
    
    def set_age(self, new_age):
        """Set a new value for age."""
        self.__age = new_age

    # Getter methods
    def get_name(self):
        """Return the person's name."""
        return self.__name
        
    def get_age(self):
        """Return the person's age."""
        return self.__age


if __name__ == "__main__":
    # Create a Person object
    person = Person("Alice", 30)

    # Change the 'name' and 'age' using setter methods
    person.set_name("Bob")
    person.set_age(25)

    # Print the 'name' and 'age' using getter methods
    print("Name:", person.get_name(), ", Age:", person.get_age())
