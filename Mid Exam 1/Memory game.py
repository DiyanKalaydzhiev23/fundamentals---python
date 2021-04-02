def check_for_cheats():
    global player_choice
    cheating = False
    player_choice = [int(el) for el in player_choice]
    if player_choice[0] == player_choice[1]:
        cheating = True
    elif player_choice[0] < 0 or player_choice[1] < 0:
        cheating = True
    elif player_choice[0] >= len(elements) or player_choice[1] >= len(elements):
        cheating = True
    return cheating


elements = input().split()
command = input()
moves = 0

while command != "end":
    player_choice = command.split()
    first = int(player_choice[0])
    second = int(player_choice[1])
    half = int(len(elements)/2)
    moves += 1
    cheats = check_for_cheats()

    if cheats:
        print("Invalid input! Adding additional elements to the board")
        elements.insert(half, f"-{moves}a")
        elements.insert(half, f"-{moves}a")
    elif elements[first] == elements[second]:
        print(f"Congrats! You have found matching elements - {elements[first]}!")
        el = elements[first]
        elements.remove(el)
        elements.remove(el)
    else:
        print("Try again!")

    if not elements:
        print(f"You have won in {moves} turns!")
        break
    command = input()
if elements:
    print(f"Sorry you lose :(\n{' '.join(elements)}")
