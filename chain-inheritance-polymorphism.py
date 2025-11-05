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


class Researcher(Teacher):
    """Represents a researcher, inherits from Teacher."""

    def __init__(self, name, age, subject, field):
        """Initialize a Researcher with name, age, subject, and field."""
        super().__init__(name, age, subject)
        self.field = field

    def display(self):
        """Display the researcher's details, including research field."""
        super().display()
        print(f"Field: {self.field}")


def main():
    """Demonstrate inheritance and method overriding."""
    person1 = Student("Alice", 30, "Computer Science")
    person2 = Teacher("Bob", 25, "Mathematics")
    researcher = Researcher("Eve", 35, "Machine Learning", "Artificial Intelligence")

    person1.display()
    print()  # Blank line for readability
    person2.display()
    print()
    researcher.display()


if __name__ == "__main__":
    main()
