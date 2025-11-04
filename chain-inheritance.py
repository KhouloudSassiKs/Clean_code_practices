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
        """Display the student's details."""
        super().display()
        print(f"Major: {self.major}")


class GraduateStudent(Student):
    """A class representing a graduate student, inherited from Student."""

    def __init__(self, name, age, major, thesis_title):
        """Initialize a GraduateStudent with name, age, major, and thesis title."""
        super().__init__(name, age, major)
        self.thesis_title = thesis_title

    def display(self):
        """Display the graduate student's full details, including thesis title."""
        super().display()
        print(f"Thesis Title: {self.thesis_title}")


if __name__ == "__main__":
    # Create an instance of GraduateStudent
    graduate_student = GraduateStudent(
        "Alice", 28, "Biology", "The Effect of Sunlight on Plant Growth"
    )

    # Display the graduate student's details
    graduate_student.display()
