inventory = input().split(", ")
command = input().split(" - ")

while True:
    item = command[1]
    if "Collect" in command:
        if item not in inventory:
            inventory.append(item)
    elif "Drop" in command:
        if item in inventory:
            inventory.remove(item)
    elif "Combine Items" in command:
        items_split = item.split(":")
        old_item = items_split[0]
        new_item = items_split[1]
        if old_item in inventory:
            old_index = inventory.index(old_item)
            inventory.insert(old_index+1, new_item)
    elif "Renew" in command:
        if item in inventory:
            item_index = inventory.index(item)
            inventory.append(inventory.pop(item_index))
    check_com = input()
    if check_com == "Craft!":
        break
    command = check_com.split(" - ")

print(", ".join(inventory))
