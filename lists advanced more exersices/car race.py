import math
road = [int(num) for num in input().split()]
finnish_line = math.floor(len(road)/2)
time_left = 0
time_right = 0

for i in range(0, finnish_line):
    if road[i] != 0:
        time_left += road[i]
    else:
        time_left *= 0.80

for i in range(len(road)-1, finnish_line, -1):
    if road[i] != 0:
        time_right += road[i]
    else:
        time_right *= 0.80

if time_right > time_left:
    print(f"The winner is left with total time: {time_left:.1f}")
else:
    print(f"The winner is right with total time: {time_right:.1f}")
