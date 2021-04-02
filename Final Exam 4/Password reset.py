text = list(input())
command = input().split()

while command[0] != "Done":
    if command[0] == "TakeOdd":
        odds = []
        [odds.append(text[i]) for i in range(len(text)) if i % 2 != 0]
        text = odds
    elif command[0] == "Cut":
        index, length = int(command[1]), int(command[2])
        [text.pop(index) for i in range(index, index+length)]
    elif command[0] == "Substitute":
        substring, substitute = command[1], command[2]
        text = ''.join(text)
        if substring in text:
            text = text.replace(substring, substitute)
            text = list(text)
        else:
            print("Nothing to replace!")
            text = list(text)
            command = input().split()
            continue

    print(''.join(text))
    command = input().split()

print(f"Your password is: {''.join(text)}")
