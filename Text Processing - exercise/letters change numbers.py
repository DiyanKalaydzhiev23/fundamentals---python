import math
choices = input().split()
total_result = 0

for el in choices:
    number = int(el[1:len(el)-1])
    if el[0].isupper():
        pos = ord(el[0]) - 64
        current_result = number / pos
    else:
        pos = ord(el[0]) - 96
        current_result = number * pos
    if el[-1].isupper():
        pos = ord(el[-1]) - 64
        current_result -= pos
    else:
        pos = ord(el[-1]) - 96
        current_result += pos
    total_result += current_result

print(f"{total_result:.2f}")
