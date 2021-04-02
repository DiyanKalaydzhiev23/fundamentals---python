numbers = [n for n in input().split(" ")]
command = input().split()

while "end" not in command:
    if "reverse" in command:
        start = int(command[2])
        end = start + int(command[4])
        numbers[start:end] = numbers[start:end][::-1]
    elif "sort" in command:
        start = int(command[2])
        end = start + int(command[4])
        slice_n = numbers[start:end]
        slice_n.sort()
        numbers[start:end] = slice_n
    elif "remove" in command:
        removable = int(command[1])
        for i in range(removable):
            numbers.pop(0)

    command = input().split()

print(f"{', '.join(list(map(lambda x: str(x), numbers)))}")
