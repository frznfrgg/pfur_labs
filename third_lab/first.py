from typing import List, Union


class Student:
    def __init__(self, name: str, student_id: Union[str, int], grades: List[int]):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def add_grade(self, grade: int):
        if isinstance(grade, int) and 0 <= grade <= 10:
            self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def display_info(self):
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
