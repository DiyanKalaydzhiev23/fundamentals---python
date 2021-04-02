numbers = [int(num) for num in input().split(".")]
numbers = numbers[::-1]

for i in range(len(numbers)):
    if numbers[i] == 9:
        numbers[i] = 0
    else:
        numbers[i] += 1
        break

numbers = numbers[::-1]
numbers = [str(num) for num in numbers]
print(".".join(numbers))
