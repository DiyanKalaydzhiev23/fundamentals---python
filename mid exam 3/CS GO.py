initial_energy = int(input())
won = 0

while True:
    if won % 3 == 0:
        initial_energy += won
    command = input()
    if command == "End of battle":
        print(f"Won battles: {won}. Energy left: {initial_energy}")
        break
    enemy = int(command)
    if initial_energy - enemy >= 0:
        won += 1
        initial_energy -= enemy
    else:
        print(f"Not enough energy! Game ends with {won} won battles and {initial_energy} energy")
        break
