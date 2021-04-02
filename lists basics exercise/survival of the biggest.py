import sys
numbers = input().split()
num = int(input())
for i in range(num):
    min_num = sys.maxsize
    for el in numbers:
        element = int(el)
        if element < min_num:
            min_num = element
    numbers.remove(str(min_num))
for index in range(len(numbers)):
    numbers[index] = int(numbers[index])
print(numbers)
