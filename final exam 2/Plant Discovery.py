plants = {}

for _ in range(int(input())):
    info = input().split("<->")
    if info[0] in plants:
        plants[info[0]][0] = int(info[1])
    else:
        plants[info[0]] = [int(info[1]), []]

command = input().split(":")

while command[0] != "Exhibition":
    tokens = command[1].split(" - ")
    plant = tokens[0].strip()

    if plant not in plants:
        print("error")
    elif command[0] == "Rate":
        rating = tokens[1]
        plants[plant][1].append(int(rating))
    elif command[0] == "Update":
        new_rarity = int(tokens[1])
        plants[plant][0] = new_rarity
    elif command[0] == "Reset":
        plants[plant][1] = []

    command = input().split(":")

for plant in plants:
    if plants[plant][1]:
        plants[plant][1] = sum(plants[plant][1]) / len(plants[plant][1])
    else:
        plants[plant][1] = 0

plants = dict(sorted(plants.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True))
print(f"Plants for the exhibition:")
[print(f"- {el}; Rarity: {plants[el][0]}; Rating: {float(plants[el][1]):.2f}") for el in plants]
