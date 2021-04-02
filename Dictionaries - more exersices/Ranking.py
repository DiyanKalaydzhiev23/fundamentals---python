contests_data = {}
data = input().split(":")
participants = {}

while "end of contests" not in data:
    name = data[0]
    password = data[1]
    contests_data[name] = password
    data = input().split(":")

data = input().split("=>")

while "end of submissions" not in data:
    contest = data[0]
    password = data[1]
    name = data[2]
    points = int(data[3])
    is_same = False

    if contest in contests_data:
        if password in contests_data[contest]:
            if name in participants:
                index = 0
                for info in participants[name]:
                    if info[0] == contest:
                        is_same = True
                        if points > info[1]:
                            participants[name][index][1] = points
                    index += 1
                if not is_same:
                    participants[name].append([contest, points])
            else:
                participants[name] = []
                participants[name].append([contest, points])

    data = input().split("=>")

best_total = 0
best_user = ""

for name in participants:
    current_total = 0
    current_user = name
    for info in participants[name]:
        current_total += info[1]
    if current_total > best_total:
        best_total = current_total
        best_user = current_user

print(f"Best candidate is {best_user} with total {best_total} points.")
print("Ranking:")

participants = dict(sorted(participants.items(), key=lambda x: x[0]))

for name in participants:
    print(name)
    sorted_contests = sorted(participants[name], key=lambda x: -x[1])
    for i in range(len(sorted_contests)):
        print(f"#  {sorted_contests[i][0]} -> {sorted_contests[i][1]}")
