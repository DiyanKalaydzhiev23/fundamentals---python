def check_for_null():
    global data
    if data[2] == "null":
        data[2] = "45"
    if data[3] == "null":
        data[3] = "250"
    if data[4] == "null":
        data[4] = "10"


n = int(input())
dragons = {}
types_dragons = {}

for _ in range(n):
    data = input().split(" ")
    name = data[1]
    type_dragon = data[0]
    check_for_null()
    damage = int(data[2])
    health = int(data[3])
    armor = int(data[4])
    id_dragon = name + "-" + type_dragon

    if id_dragon not in dragons:
        dragons[id_dragon] = [damage, health, armor]
        if type_dragon not in types_dragons:
            types_dragons[type_dragon] = [damage, health, armor, 1]
        else:
            types_dragons[type_dragon][0] += damage
            types_dragons[type_dragon][1] += health
            types_dragons[type_dragon][2] += armor
            types_dragons[type_dragon][3] += 1
    else:
        damage_diff = damage - dragons[id_dragon][0]
        health_diff = health - dragons[id_dragon][1]
        armor_diff = armor - dragons[id_dragon][2]
        dragons[id_dragon][0] = damage
        dragons[id_dragon][1] = health
        dragons[id_dragon][2] = armor
        types_dragons[type_dragon][0] += damage_diff
        types_dragons[type_dragon][1] += health_diff
        types_dragons[type_dragon][2] += armor_diff

for type_dragon in types_dragons:
    values = types_dragons[type_dragon]
    avg_damage = values[0] / values[3]
    avg_health = values[1] / values[3]
    avg_armor = values[2] / values[3]
    print(f"{type_dragon}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    list_of_dragons = []

    for dragon in dragons:
        info = dragon.split("-")
        name = info[0]
        dragon_type = info[1]
        if dragon_type == type_dragon:
            list_of_dragons.append([name, dragons[dragon][0], dragons[dragon][1], dragons[dragon][2]])

    list_of_dragons = sorted(list_of_dragons, key=lambda x: x[0])

    for info in list_of_dragons:
        name = info[0]
        damage = info[1]
        health = info[2]
        armor = info[3]
        print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")
