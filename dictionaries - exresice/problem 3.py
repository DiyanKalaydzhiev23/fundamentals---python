cards = input().split(":")
command = input().split()
deck = []

while "Ready" not in command:
    card_name = command[1]
    type_command = command[0]

    if type_command == 'Add':
        if card_name in cards:
            deck.append(card_name)
        else:
            print("Card not found.")
    elif type_command == "Insert":
        index = int(command[2])
        if (card_name in cards) and (0 <= index < len(deck)):
            deck.insert(index, card_name)
        else:
            print("Error!")
    elif type_command == "Remove":
        if card_name in deck:
            deck.remove(card_name)
        else:
            print("Card not found.")
    elif type_command == "Swap":
        card_name_2 = command[2]
        first = deck.index(card_name)
        second = deck.index(card_name_2)
        deck[first], deck[second] = deck[second], deck[first]
    elif type_command == "Shuffle":
        deck = deck[::-1]

    command = input().split()

print(f"{' '.join(deck)}")
