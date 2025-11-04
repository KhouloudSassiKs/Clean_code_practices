class Person:
    """A class representing a person with a name and age."""

    def __init__(self, name, age):
        """Initialize a Person with name and age."""
        self.name = name
        self.age = age

    def display(self):
        """Display the person's details."""
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    """A class representing a student, inherited from Person."""

    def __init__(self, name, age, major):
        """Initialize a Student with name, age, and major."""
        super().__init__(name, age)
        self.major = major

    def display(self):
        """Display the student's details, including major."""
        super().display()  # Reuse Person’s display for cleaner inheritance
        print(f"Major: {self.major}")


if __name__ == "__main__":
    # Create and display a Student object
    student = Student("Khouloud", 31, "Computer Science")
    student.display()
