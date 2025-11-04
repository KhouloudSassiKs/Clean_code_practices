class Person:
    """A class representing a person with a name and age."""

    def __init__(self, name, age):
        """Initialize a Person object with name and age."""
        self.name = name
        self.age = age

    def display(self):
        """Display the person's details."""
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    """A class representing a student, inherited from Person."""

    def __init__(self, name, age, major, university):
        """Initialize a Student object with name, age, major, and university."""
        super().__init__(name, age)
        self.major = major
        self.university = university

    def display(self):
        """Display the student's details, including university."""
        super().display()
        print(f"Major: {self.major}, University: {self.university}")


if __name__ == "__main__":
    # Create a Student object with all required attributes
    student = Student("Khouloud", 31, "Computer Science", "Stanford University")

    # Display the student's information
    student.display()
