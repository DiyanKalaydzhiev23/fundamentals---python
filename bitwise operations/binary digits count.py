number = int(input())
n_to_count = int(input())
counter = 0

while number > 0:
    result = number % 2
    number //= 2
    if result == n_to_count:
        counter += 1

print(counter)
