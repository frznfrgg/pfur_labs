import csv

from utils.student_utils import StudentUtils

with open("data/students.csv", mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

analyzer = StudentUtils()
top_students = analyzer.get_top_students(data, 2)
average_age = analyzer.get_average_age(data)
filtered_students = analyzer.filter_students_by_grade(data, 4.0)
sorted_students = sorted(data, key=lambda x: float(x["Возраст"]))

print("Sorted students by age:", sorted_students)

with open("results/report.txt", "w") as f:
    f.write(f"Top students: {top_students}\n")
    f.write(f"Average age: {average_age}\n")
    f.write(f"Filtered students: {filtered_students}\n")
    f.write(f"Sorted students by age: {sorted_students}")
