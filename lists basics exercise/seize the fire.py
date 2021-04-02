fire_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
is_valid = False
print("Cells:")
for fires in range(len(fire_cells)):
    one_cell = fire_cells.pop(0)
    t_value_cell = one_cell.split()
    if water >= int(t_value_cell[2]):
        if t_value_cell[0] == "High" and 81 <= int(t_value_cell[2]) <= 125:
            is_valid = True
        elif t_value_cell[0] == "Medium" and 51 <= int(t_value_cell[2]) <= 80:
            is_valid = True
        elif t_value_cell[0] == "Low" and 1 <= int(t_value_cell[2]) <= 50:
            is_valid = True
    if is_valid:
        print(f" - {t_value_cell[2]}")
        water -= int(t_value_cell[2])
        total_fire += int(t_value_cell[2])
        effort += 0.25 * int(t_value_cell[2])
        is_valid = False
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
