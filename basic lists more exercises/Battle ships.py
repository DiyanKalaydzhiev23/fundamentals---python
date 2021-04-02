n = int(input())
all_rows = []
destroyed = 0
for rows in range(1, n + 1):
    all_rows += [input()]
attack_log = input().split()
for index in range(len(attack_log)):
    one_list_row = ""
    row_atk, col_atk = attack_log[index].split("-")
    row = all_rows[int(row_atk)].split()
    result = int(row[int(col_atk)])
    if result > 0:
        result -= 1
        for i in range(len(row)):
            if i == int(col_atk):
                to_remove = row[int(col_atk)]
                row.remove(to_remove)
                row.insert(int(col_atk), result)
                for el in row:
                    one_list_row += ' ' + str(el)
                all_rows[int(row_atk)] = one_list_row
                if result == 0:
                    destroyed += 1
                    break
print(destroyed)
