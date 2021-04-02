message = list(input())
command = input().split(":|:")

while command[0] != "Reveal":
    if command[0] == "InsertSpace":
        message.insert(int(command[1]), " ")
    elif command[0] == "Reverse":
        substring = command[1]
        message = "".join(message)
        if substring in message:
            message = list(message.replace(substring, "", 1))
            substring = substring[::-1]
            message.extend(substring)
        else:
            print("error")
            message = list(message)
            command = input().split(":|:")
            continue
    elif command[0] == "ChangeAll":
        message = ''.join(message)
        message = message.replace(command[1], command[2])
        message = list(message)
    command = input().split(":|:")
    print(''.join(message))

print(f"You have a new text message: {''.join(message)}")
