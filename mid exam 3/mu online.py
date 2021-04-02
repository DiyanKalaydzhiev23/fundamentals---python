initial_health = 100
initial_bitcoins = 0
dungenos_rooms = input().split("|")
alive = True

for i in range(len(dungenos_rooms)):
    room = dungenos_rooms[i].split()
    type_command = room[0]
    nums = int(room[1])
    if type_command == "potion":
        if nums + initial_health > 100:
            healed = 100 - initial_health
            initial_health = 100
        else:
            initial_health += nums
            healed = nums
        print(f"You healed for {healed} hp.")
        print(f"Current health: {initial_health} hp.")
    elif type_command == "chest":
        initial_bitcoins += nums
        print(f"You found {nums} bitcoins.")
    else:
        if initial_health - nums <= 0:
            print(f"You died! Killed by {type_command}.")
            print(f"Best room: {i + 1}")
            alive = False
            break
        else:
            initial_health -= nums
            print(f"You slayed {type_command}.")

if alive:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
