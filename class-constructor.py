class Person:
    """A class representing a person with a name and age."""

    # TODO: Implement a constructor that initializes 'name' and 'age'
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # TODO: Implement a 'display' method that prints 'name' and 'age'
    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")


if __name__ == "__main__":
    # TODO: Create a Person object with name "Alice" and age 30
    person = Person("Alice", 30)

    # TODO: Call the 'display' method on this object to print the details
    person.display()
