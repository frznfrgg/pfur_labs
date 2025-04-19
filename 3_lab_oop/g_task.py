from typing import List, Union

from a_task import Student
from b_task import Teacher


class Assistant(Teacher, Student):
    """Simple assistant class"""

    def __init__(
        self,
        student_name: str,
        student_id: Union[str, int],
        student_grades: List[int],
        teacher_name: str,
        teacher_age: int,
        teacher_subject: str,
    ):
        """Initializes assistant class

        Args:
            student_name (str): name of a student
            student_id (Union[str, int]): students id
            student_grades (List[int]): grades of a student
            teacher_name (str): teachers name
            teacher_age (int): teachers age
            teacher_subject (str): teachers subject
        """
        student = Student.__init__(self, student_name, student_id, student_grades)

        Teacher.__init__(self, teacher_name, teacher_age, teacher_subject, [student])
        Student.__init__(self, student_name, student_id, student_grades)

        self.teacher_name = teacher_name
        self.student_name = student_name

    def help_student(self):
        """Prints assistants statistics"""
        print(
            f"Assistant of teacher {self.teacher_name} is helping a student {self.student_name}."
        )
        print("Studnet statistics:")
        self.display_info()
