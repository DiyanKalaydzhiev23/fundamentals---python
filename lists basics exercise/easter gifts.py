command = input().split()
products_list = []
while command[0] != "No":
    if command[0] == "OutOfStock":
        product = command.pop(1)
        if product in products_list:
            for index, value in enumerate(products_list):
                if value == product:
                    products_list[index] = "None"
    elif command[0] == "Required":
        product = command.pop(1)
        index = int(command.pop(1))
        if 0 <= index <= len(products_list):
            if index == len(products_list):
                index -= 1
            products_list[index] = product
    elif command[0] == "JustInCase":
        product = command.pop(1)
        products_list[-1] = product
    else:
        products_list = command
    command = input().split()
while "None" in products_list:
    products_list.remove("None")
print(" ".join(products_list))
