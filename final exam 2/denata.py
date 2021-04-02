n = int(input())
plants_rarities = {}
plants_ratings = {}
for i in range(n):
    plant, rarity = input().split("<->")
    plants_rarities[plant] = int(rarity)

command = input()
while not command == "Exhibition":
    curr_command = command.split(": ")
    task = curr_command[0]
    if task == "Rate":
        plant, rating = curr_command[1].split(" - ")
        if plant in plants_rarities:
            if plant not in plants_ratings:
                plants_ratings[plant] = []
            plants_ratings[plant].append(float(rating))
        else:
            print("error")
    elif task == "Update":
        plant, new_rarity = curr_command[1].split(" - ")
        if plant in plants_rarities:
            plants_rarities[plant] = int(new_rarity)
        else:
            print("error")
    elif task == "Reset":
        plant = curr_command[1]
        if plant in plants_ratings:
            plants_ratings[plant].clear()
        else:
            print("error")
    else:
        print("error")
    command = input()

plants = {}
for plant, rarity in plants_rarities.items():
    if plants_ratings[plant]:
        avg_rating = sum(plants_ratings[plant]) / len(plants_ratings[plant])
    else:
        avg_rating = 0.00
    plants[plant] = [rarity, avg_rating]

print(f"Plants for the exhibition:")
for plant, info in sorted(plants.items(), key=lambda kvp: (kvp[1][0], kvp[1][1]), reverse= True):
    print(f"- {plant}; Rarity: {info[0]}; Rating: {info[1]:.2f}")