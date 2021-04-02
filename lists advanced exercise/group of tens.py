numbers = [int(num) for num in input().split(", ")]
boundary = 10

while numbers:
    current_list = []
    index = 0
    while index < len(numbers):
        num = numbers[index]
        if num <= boundary:
            current_list.append(num)
            numbers.remove(numbers[index])
            continue
        index += 1
    print(f"Group of {boundary}'s: {current_list}")
    boundary += 10
