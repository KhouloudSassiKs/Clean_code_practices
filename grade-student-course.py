"""
This script models a course management system with separate classes
for Course, Students, and Grades for better modularity.
"""

class Students:
    def __init__(self):
        """Initialize an empty list of student names."""
        self.students = []
    
    def add_student(self, student_name):
        """Add a student name to the list."""
        self.students.append(student_name)
    
    def get_all_students(self):
        """Return the list of all students."""
        return self.students


class Grades:
    def __init__(self):
        """Initialize an empty dictionary to store grades by student name."""
        self._grades = {}
    
    def add_grade(self, student_name, grade):
        """Assign a grade to a student."""
        self._grades[student_name] = grade 
    
    def print_student_grades(self, students):
        """Print each student's grade."""
        for student in students:
            print(f"Student: {student}, Grade: {self._grades.get(student)}")


class Course:
    def __init__(self, name, students=None, grades=None):
        """Initialize a course with a name, optional Students and Grades objects."""
        self.name = name
        self.students = students if students else Students()
        self.grades = grades if grades else Grades()
    
    def add_student(self, student_name):
        """Add a student to the course."""
        self.students.add_student(student_name)
    
    def assign_grade(self, student_name, grade):
        """Assign a grade to a student in this course."""
        self.grades.add_grade(student_name, grade)
    
    def print_student_grades(self):
        """Print all student grades for this course."""
        self.grades.print_student_grades(self.students.get_all_students())


def main():
    # Create students and course
    students = Students()
    students.add_student("John Doe")
    students.add_student("Jane Smith")

    grades = Grades()
    course = Course("History 101", students, grades)

    # Assign grades
    course.assign_grade("John Doe", 85.5)
    course.assign_grade("Jane Smith", 92.0)

    # Print course details
    print(f"Course: {course.name}")
    course.print_student_grades()
    

if __name__ == "__main__":
    main()
