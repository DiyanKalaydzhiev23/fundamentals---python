import math

students = int(input())
lectures = int(input())
bonus = int(input())
max_bonus = 0
max_lectures = 0

for _ in range(students):
    attendances = int(input())
    total_bonus = attendances / lectures * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_lectures = attendances

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_lectures} lectures.")
