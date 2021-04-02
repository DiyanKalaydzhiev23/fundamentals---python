wagons = int(input())
wagons_list = [0 for _ in range(wagons)]
command = input().split()

while "End" not in command:
    if "add" in command:
        wagons_list[-1] += int(command[1])
    elif "insert" in command:
        wagons_list[int(command[1])] += int(command[2])
    elif "leave" in command:
        wagons_list[int(command[1])] -= int(command[2])
    command = input().split()

print(wagons_list)
