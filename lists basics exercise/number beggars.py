numbers = input().split(", ")
beggars = int(input())
stolen_sum = []

for i in range(beggars):
    current_sum = 0
    index = i
    while True:
        if index > len(numbers) - 1:
            break
        current_sum += int(numbers[index])
        if index + beggars > len(numbers) - 1:
            break
        index += beggars
    stolen_sum.append(current_sum)

print(stolen_sum)
