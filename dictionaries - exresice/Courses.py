courses = {}
data = input().split(" : ")

while "end" not in data:
    course = data[0]
    user = data[1]

    if course not in courses:
        courses[course] = []
        courses[course].append(user)
    else:
        courses[course].append(user)

    data = input().split(" : ")

courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))

for key, value in courses.items():
    courses[key] = list(sorted(value))
    print(f"{key}: {len(courses[key])}")
    [print(f"-- {name}") for name in courses[key]]
