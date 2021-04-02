stops = list(input())
command = input().split(":")

while command[0] != "Travel":
    if command[0] == "Add Stop":
        if 0 <= int(command[1]) < len(stops):
            index = int(command[1])
            for letter in command[2]:
                stops.insert(index, letter)
                index += 1
    elif command[0] == "Remove Stop":
        if 0 <= int(command[1]) < len(stops) and 0 <= int(command[2]) < len(stops):
            [stops.pop(int(command[1])) for i in range(int(command[1]), int(command[2])+1)]
    elif command[0] == "Switch":
        stops = ''.join(stops)
        if command[1] in stops:
            stops = stops.replace(command[1], command[2])
        stops = list(stops)
    print(''.join(stops))
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {''.join(stops)}")
