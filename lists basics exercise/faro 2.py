deck = input().split()
shuffles = int(input())
max_index = len(deck)
half_index = int(max_index / 2)

for _ in range(shuffles):
    side_a = []
    side_b = []
    current_list = []
    for i in range(0, half_index):
        side_a.append(deck[i])
    for i in range(half_index, max_index):
        side_b.append(deck[i])
    for i in range(max_index):
        if i % 2 == 0:
            current_list.append(side_a.pop(0))
        elif i % 2 != 0:
            current_list.append((side_b.pop(0)))
    deck = current_list

print(deck)
