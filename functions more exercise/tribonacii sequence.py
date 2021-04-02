num = int(input())
list_nums = []


def sequence():
    next_num = 0
    if len(list_nums) < 3:
        if len(list_nums) == 2:
            next_num = list_nums[-1] + list_nums[-2]
        else:
            next_num = 1
    else:
        next_num = list_nums[-1] + list_nums[-2] + list_nums[-3]
    list_nums.append(next_num)
    return next_num


for n in range(num):
    print(sequence(), end=" ")
