from a_task import Student


class Person:
    """Simple person class"""

    def __init__(self, name: str, age: int):
        """Initializes a person class

        Args:
            name (str): persons name
            age (int): persons age
        """
        self.name = name
        self.age = age


class Teacher(Person):
    """Simple teacher class inherited from Person class"""

    def __init__(self, name: str, age: int, subject: str, students: list):
        """Initializes a Teacher class

        Args:
            name (str): teachers name
            age (int): teachers age
            subject (str): teachers subject
            students (list): teachers students
        """
        super().__init__(name, age)
        self.subject = subject
        self.students = students

    def add_student(self, student: Student):
        """Adds student to class

        Args:
            student (Student): student to add
        """
        self.students.append(student)

    def remove_student(self, student_id: int):
        """Removes student from class

        Args:
            student_id (int): id of a student to be removed
        """
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                break

    def list_students(self):
        """prints students in a class"""
        [print(student.display_info()) for student in self.students]
