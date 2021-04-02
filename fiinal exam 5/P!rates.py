cities = {}
command = input().split("||")

while command[0] != "Sail":
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city in cities:
        cities[city][0] += population
        cities[city][1] += gold
    else:
        cities[city] = [population, gold]
    command = input().split("||")

command = input().split("=>")

while command[0] != "End":
    if command[0] == "Plunder":
        town, people, gold = command[1], int(command[2]), int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town][0] -= people
        cities[town][1] -= gold
        if cities[town][0] == 0 or cities[town][1] == 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    elif command[0] == "Prosper":
        town, gold = command[1], int(command[2])
        if gold >= 0:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")
    command = input().split("=>")

if cities:
    cities = dict(sorted(cities.items(), key=lambda x: (-x[1][1], x[0])))
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    [print(f"{city} -> Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg") for city in cities]
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
