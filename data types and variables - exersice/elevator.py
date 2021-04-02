people = int(input())
capacity = int(input())
courses = 0
while people != 0:
    if people < capacity:
        people -= people
    else:
        people -= capacity
    courses += 1
print(courses)
