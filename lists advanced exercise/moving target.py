targets = [int(target) for target in input().split()]
command = input().split()

while "End" not in command:
    index = int(command[1])
    if "Shoot" in command:
        power = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif "Add" in command:
        value = int(command[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif "Strike" in command:
        radius = int(command[2])
        if (index - radius) >= 0 and (index + radius) < len(targets):
            for _ in range(radius):
                targets.pop(index+1)
            targets.pop(index)
            for _ in range(radius):
                targets.pop(index-1)
        else:
            print("Strike missed!")
    command = input().split()

targets = [str(target) for target in targets]
print("|".join(targets))
