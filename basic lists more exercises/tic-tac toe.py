first_won = False
second_won = False
for i in range(1, 4):
    if i == 1:
        first_lane = input().split()
    elif i == 2:
        second_line = input().split()
    elif i == 3:
        third_line = input().split()
for i in range(3):
    if first_lane.count("1") == 3 or second_line.count("1") == 3 or third_line.count("1") == 3:
        first_won = True
    elif first_lane.count("2") == 3 or second_line.count("2") == 3 or third_line.count("2") == 3:
        second_won = True
    elif i == 0:
        if first_lane[i] == "1" and second_line[i + 1] == "1" and third_line[i + 2] == "1":
            first_won = True
        elif first_lane[i] == "2" and second_line[i + 1] == "2" and third_line[i + 2] == "2":
            second_won = True
    elif i == 1:
        if first_lane[i] == "1" and second_line[i] == "1" and third_line[i] == "1":
            first_won = True
        elif first_lane[i] == "2" and second_line[i] == "2" and third_line[i] == "2":
            second_won = True
        if first_lane[i - 1] == "1" and second_line[i - 1] == "1" and third_line[i - 1] == "1":
            first_won = True
        elif first_lane[i - 1] == "2" and second_line[i - 1] == "2" and third_line[i - 1] == "2":
            second_won = True
        if first_lane[i + 1] == "1" and second_line[i + 1] == "1" and third_line[i + 1] == "1":
            first_won = True
        elif first_lane[i + 1] == "2" and second_line[i + 1] == "2" and third_line[i + 1] == "2":
            second_won = True
    elif i == 2:
        if first_lane[i] == "1" and second_line[i - 1] == "1" and third_line[i - 2] == "1":
            first_won = True
        elif first_lane[i] == "1" and second_line[i - 1] == "1" and third_line[i - 2] == "1":
            second_won = True
if first_won:
    print("First player won")
elif second_won:
    print("Second player won")
else:
    print("Draw!")
