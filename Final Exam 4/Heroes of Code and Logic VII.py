heroes = {}

for _ in range(int(input())):
    name, hp, mp = input().split()
    heroes[name] = [int(hp), int(mp)]

command = input().split(" - ")

while command[0] != "End":
    if command[0] == "CastSpell":
        name, mp, spell = command[1], int(command[2]), command[3]
        if heroes[name][1] >= mp:
            heroes[name][1] -= mp
            print(f"{name} has successfully cast {spell} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")
    elif command[0] == "TakeDamage":
        name, damage, attacker = command[1], int(command[2]), command[3]
        heroes[name][0] -= damage
        if heroes[name][0] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")
        else:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")
    elif command[0] == 'Recharge':
        name, amount = command[1], int(command[2])
        if heroes[name][1] + amount > 200:
            print(f"{name} recharged for {amount - (heroes[name][1]+amount-200)} MP!")
            heroes[name][1] = 200
        else:
            print(f"{name} recharged for {amount} MP!")
            heroes[name][1] += amount
    elif command[0] == "Heal":
        name, amount = command[1], int(command[2])
        if heroes[name][0] + amount > 100:
            print(f"{name} healed for {amount - (heroes[name][0]+amount-100)} HP!")
            heroes[name][0] = 100
        else:
            print(f"{name} healed for {amount} HP!")
            heroes[name][0] += amount

    command = input().split(" - ")

heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])))
[print(f"{hero}\n  HP: {heroes[hero][0]}\n  MP: {heroes[hero][1]}") for hero in heroes]
