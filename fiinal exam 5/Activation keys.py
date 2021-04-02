activation_key = list(input())
command = input().split(">>>")

while command[0] != "Generate":
    if command[0] == "Contains":
        activation_key = ''.join(activation_key)
        if command[1] in activation_key:
            print(f"{activation_key} contains {command[1]}")
        else:
            print("Substring not found!")
        activation_key = list(activation_key)
    elif command[0] == "Flip":
        case, start, end = command[1], int(command[2]), int(command[3])
        for i in range(start, end):
            if case == "Upper":
                activation_key[i] = activation_key[i].upper()
            else:
                activation_key[i] = activation_key[i].lower()
        print(''.join(activation_key))
    elif command[0] == "Slice":
        start, end = int(command[1]), int(command[2])
        [activation_key.pop(start) for _ in range(start, end)]
        print(''.join(activation_key))
    command = input().split(">>>")

print(f"Your activation key is: {''.join(activation_key)}")
