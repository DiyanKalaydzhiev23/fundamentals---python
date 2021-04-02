word = input()
index_list = list([])
for index, value in enumerate(word):
    ascii_number = ord(value)
    if 65 <= ascii_number <= 90:
        index_list.append(index)
print(index_list)
