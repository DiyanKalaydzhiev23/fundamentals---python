first = ord(input())
second = ord(input())
sum_of_letters = 0

for el in input():
    if first < ord(el) < second:
        sum_of_letters += ord(el)

print(sum_of_letters)
