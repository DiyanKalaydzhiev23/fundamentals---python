numbers = input().split(",")
zero_list = []
others_list = []
for el in numbers:
    element = int(el)
    if element == 0:
        zero_list.append(element)
    else:
        others_list.append(element)
others_list += zero_list
print(others_list)
