n = int(input())
matrix = [row for lists in range(n) for index, row in enumerate(input())]
last_pos_possible = []
pos = ""
last_count_mov = 0

for i in range(len(matrix)):
    row = matrix[i]
    if "k" in row:
        k_row_i = row.index("k")
        pos = f"{i}:{k_row_i}"
        break

def check_for_ops():
    global k_row_i, row

    if matrix[row][k_row_i+1]