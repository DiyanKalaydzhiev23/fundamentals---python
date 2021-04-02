quantity = int(input())
days_left = int(input())
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
gained_spirit = 0
total_cost = 0
for i in range(1, days_left + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_cost += ornament_set * quantity
        gained_spirit += 5
    if i % 3 == 0:
        total_cost += (tree_skirt + tree_garlands) * quantity
        gained_spirit += 13
    if i % 5 == 0:
        total_cost += tree_lights * quantity
        gained_spirit += 17
        if i % 3 == 0:
            gained_spirit += 30
    if i % 10 == 0:
        total_cost += tree_skirt + tree_garlands + tree_lights
        if i == days_left:
            gained_spirit -= 30
        gained_spirit -= 20
print(f"Total cost: {total_cost}")
print(f"Total spirit: {gained_spirit}")
