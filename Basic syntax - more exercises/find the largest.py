number = input()
max_number = ""
number_list = list([])
max_current = 0
first_time = False
for i in range(len(number)):
    for index, value in enumerate(number):
        if not first_time:
            number_list += value
        if int(value) > max_current:
            max_current = int(value)
    max_number += str(max_current)
    first_time = True
    if str(max_current) in number_list:
        number_list.remove(str(max_current))
    max_current = 0
    number = number_list
print(max_number)