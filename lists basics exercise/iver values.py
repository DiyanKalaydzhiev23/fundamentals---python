numbers = input()
current_number = 0
normal_list = numbers.split()
opposite_list = []
for el in normal_list:
    el = int(el)
    if el < 0:
        el = abs(el)
        opposite_list.append(el)
    elif el > 0:
        current_number = -el
        opposite_list.append(-el)
    elif el == 0:
        opposite_list.append(el)
print(opposite_list)
