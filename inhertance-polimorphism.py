class Person:
    """Base class representing a person."""

    def __init__(self, name, age):
        """Initialize a Person with name and age."""
        self.name = name
        self.age = age

    def display(self):
        """Display the person's details."""
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    """Represents a student, inherits from Person."""

    def __init__(self, name, age, major):
        """Initialize a Student with name, age, and major."""
        super().__init__(name, age)
        self.major = major

    def display(self):
        """Display the student's details."""
        super().display()
        print(f"Major: {self.major}")


class Teacher(Person):
    """Represents a teacher, inherits from Person."""

    def __init__(self, name, age, subject):
        """Initialize a Teacher with name, age, and subject."""
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        """Display the teacher's details."""
        super().display()
        print(f"Subject: {self.subject}")


def main():
    """Demonstrate polymorphism with a list of Person, Student, and Teacher objects."""
    people = [
        Person("Alice", 30),
        Student("Bob", 20, "Computer Science"),
        Teacher("Charlie", 40, "Mathematics")
    ]

    for person in people:
        person.display()
        print()  # Add a blank line for readability


if __name__ == "__main__":
    main()
