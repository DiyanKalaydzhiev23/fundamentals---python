n = int(input())
all_rows = []
food = 0
no_more_total = False
no_more_for_food = False
while_i = 0
while not no_more_total:
    while_i += 1
    if while_i == 1:
        for row in range(n):
            all_rows += [input().split()]
    for i in range(n):
        one_found = False
        positions = []
        one_row = all_rows[i]
        for j in range(len(one_row)):
            number = one_row[j]
            if number == "1":
                all_rows[i].remove("1")
                all_rows[i].insert(j, "0")
                positions.append(str(j))
                one_found = True
            if number == "0" and one_found:
                break
        for k in range(len(all_rows)):
            one_row = all_rows[k]
            for j in range(one_row):
                element = one_row[j]
                index = j
                if element == '1' and (index in positions):
                    no_more_for_food = True



