from typing import List, NoReturn, Union


class Student:
    """Simple student class"""

    def __init__(self, name: str, student_id: Union[str, int], grades: List[int]):
        """Initializes a student object

        Args:
            name (str): student name
            student_id (Union[str, int]): student id
            grades (List[int]): student grades
        """
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def add_grade(self, grade: int):
        """Adds a grade to students profile

        Args:
            grade (int): a grade to add
        """
        if isinstance(grade, int) and 0 <= grade <= 10:
            self.grades.append(grade)

    def get_average(self) -> float:
        """Calculates the average grade of the student

        Returns:
            float: mean grade
        """
        return sum(self.grades) / len(self.grades)

    def display_info(self) -> NoReturn:
        """Prints students statistics

        Returns:
            NoReturn:
        """
        print(
            "Name:",
            self.name,
            "--",
            "ID:",
            str(self.student_id),
            "--",
            "Grades:",
            self.grades,
        )

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Grades: {self.grades}"

    def __len__(self):
        return len(self.grades)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False
