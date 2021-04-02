number = int(input())
counter = int(input())
number_add = number
list_numbers = [number]
for i in range(counter - 1):
    number_add += number
    list_numbers.append(number_add)
print(list_numbers)
