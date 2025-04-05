class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str, students: list):
        super().__init__(name, age)
        self.subject = subject
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                break

    def list_students(self):
        print(self.students)
