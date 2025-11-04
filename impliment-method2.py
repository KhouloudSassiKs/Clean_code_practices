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

    def __init__(self, name, age, major, student_id):
        """Initialize a Student with name, age, major, and student ID."""
        super().__init__(name, age)
        self.major = major
        self.student_id = int(student_id)  # Ensure ID is stored as an integer

    def display(self):
        """Display the student's full details in one print statement."""
        print(
            f"Name: {self.name}, Age: {self.age}, "
            f"Major: {self.major}, Student ID: {self.student_id}"
        )


if __name__ == "__main__":
    # Create a Student object with name, age, major, and student ID
    student = Student("Khouloud", 31, "Computer Science", 101)
    student.display()
