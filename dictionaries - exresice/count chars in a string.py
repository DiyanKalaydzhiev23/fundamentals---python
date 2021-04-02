char_count = {}

for index, value in enumerate(input()):
    if value == " ":
        continue
    if value in char_count:
        char_count[value] += 1
    else:
        char_count[value] = 1

[print(f"{char} -> {times}") for char, times in char_count.items()]
