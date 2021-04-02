n = int(input())
students_grades = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students_grades:
        students_grades[name] = [grade, 1]
    else:
        students_grades[name][0] += grade
        students_grades[name][1] += 1

students_grades = {name: grade[0]/grade[1] for name, grade in students_grades.items()}
students_grades = dict(filter(lambda x: x[1] >= 4.50, students_grades.items()))
students_grades = dict(sorted(students_grades.items(), key=lambda x: x[1], reverse=True))

[print(f"{name} -> {grade:.2f}") for name, grade in students_grades.items()]
