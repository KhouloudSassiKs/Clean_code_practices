class Person:
    """Base class representing a person."""

    def __init__(self, name, age):
        """Initialize a Person with name and age."""
        self.name = name
        self.age = age

    def display(self):
        """Display the person's details."""
        print(f"Name: {self.name}, Age: {self.age}")

    def introduce(self):
        """Introduce as a general person."""
        print("Hello, I am a person")


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

    def introduce(self):
        """Introduce as a student."""
        print("Hello, I am a student")


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


if __name__ == "__main__":
    # Create objects
    person1 = Student("Alice", 30, "Computer Science")
    person2 = Teacher("Bob", 25, "Mathematics")

    # Display and introduce student
    person1.display()
    person1.introduce()

    # Display and introduce teacher
    person2.display()
    person2.introduce()  # Uses Person's introduce() since not overridden
