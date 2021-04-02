def check_if_there():
    there = False
    for product in groceries:
        if product == item:
            there = True
            break
    return there


groceries = input().split("!")
command = input().split()

while "Go" not in command:
    item = command[1]

    if "Urgent" in command:
        already_there = check_if_there()
        if not already_there:
            groceries.insert(0, item)
    elif "Unnecessary" in command:
        already_there = check_if_there()
        if already_there:
            groceries.remove(item)
    elif "Correct" in command:
        new_item = command[2]
        already_there = check_if_there()
        if already_there:
            i = groceries.index(item)
            groceries[i] = new_item
    elif "Rearrange" in command:
        already_there = check_if_there()
        if already_there:
            i = groceries.index(item)
            groceries.append(groceries.pop(i))

    command = input().split()

print(f"{', '.join(groceries)}")
