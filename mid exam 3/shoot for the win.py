targets = [int(n) for n in input().split()]
command = input()
shot = 0

while command != "End":
    command = int(command)
    if 0 <= command < len(targets):
        if targets[command] == -1:
            continue
        else:
            target_value = targets[command]
            targets[command] = -1
            shot += 1
            for i in range(len(targets)):
                if targets[i] != -1:
                    if targets[i] <= target_value:
                        targets[i] += target_value
                    else:
                        targets[i] -= target_value
    command = input()

print(f"Shot targets: {shot} -> {' '.join(list(map(lambda x: str(x), targets)))}")
