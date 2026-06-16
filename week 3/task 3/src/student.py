# student.py
# This file defines a Student class and creates student objects.

class Student:
    """
    A class to represent a student.

    Attributes:
        name (str): The name of the student.
        age (int): The age of the student.
        course (str): The course the student is enrolled in.
    """

    def __init__(self, name, age, course):
        """
        Initialize the Student with name, age, and course.

        Args:
            name (str): Student's name.
            age (int): Student's age.
            course (str): Course the student is studying.
        """
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        """Display the student's information in a readable format."""
        print("---- Student Information ----")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
        print("-----------------------------")


# ----------------------------
# Create two Student objects
# ----------------------------

student1 = Student("Alice Johnson", 20, "Computer Science")
student2 = Student("Bob Smith", 22, "Data Science")

# Display information for both students
student1.display_info()
student2.display_info()
