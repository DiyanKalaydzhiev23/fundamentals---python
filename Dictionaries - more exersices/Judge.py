data = {}
individual = {}
info = input().split(" -> ")

while "no more time" not in info:
    name = info[0]
    contest = info[1]
    points = int(info[2])
    already_in = False

    if contest in data:
        for i in range(len(data[contest])):
            if name == data[contest][i][0]:
                already_in = True
                if points > data[contest][i][1]:
                    diff = points - data[contest][i][1]
                    data[contest][i][1] = points
                    individual[name] += diff
        if not already_in:
            data[contest].append([name, points])
            if name in individual:
                individual[name] += points
            else:
                individual[name] = points
    else:
        data[contest] = []
        data[contest].append([name, points])
        if name in individual:
            individual[name] += points
        else:
            individual[name] = points

    info = input().split(" -> ")

for contest in data:
    print(f"{contest}: {len(data[contest])} participants")
    sorted_contest = sorted(data[contest], key=lambda x: (-x[1], x[0]))
    for i in range(len(data[contest])):
        print(f"{i+1}. {sorted_contest[i][0]} <::> {sorted_contest[i][1]}")

print(f"Individual standings:")

sorted_individual = sorted(individual.items(), key=lambda x: (-x[1], x[0]))

for i in range(len(sorted_individual)):
    print(f"{i+1}. {sorted_individual[i][0]} -> {sorted_individual[i][1]}")
