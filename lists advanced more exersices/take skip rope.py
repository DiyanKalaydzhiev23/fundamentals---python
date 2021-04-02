num_list = []
text_list = []
result = ""

for index, symbol in enumerate(input()):
    if 48 <= ord(symbol) <= 57:
        num_list.append(int(symbol))
    else:
        text_list.append(symbol)

skip_list = []
take_list = []

for i in range(len(num_list)):
    if i % 2 == 0:
        take_list.append(num_list[i])
    else:
        skip_list.append(num_list[i])

while skip_list:
    take = take_list.pop(0)
    skip = skip_list.pop(0)
    taken_string = text_list[0:take]
    for index, value in enumerate(taken_string):
        result += value
        text_list.pop(0)
    for i in range(skip):
        if text_list:
            text_list.pop(0)

print(result)
