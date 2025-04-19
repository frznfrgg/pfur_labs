class StudentUtils:
    @staticmethod
    def get_top_students(students, n):
        top_students = sorted(
            students, key=lambda x: float(x["Средний балл"]), reverse=True
        )[:n]
        return top_students

    @staticmethod
    def get_average_age(students):
        total_age = sum(int(student["Возраст"]) for student in students)
        average_age = total_age / len(students)
        return average_age

    @staticmethod
    def filter_students_by_grade(students, min_grade):
        filtered_students = [
            student
            for student in students
            if float(student["Средний балл"]) >= min_grade
        ]
        return filtered_students
