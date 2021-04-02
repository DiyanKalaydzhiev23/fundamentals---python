player_pool = {}
player_total = {}
command = input().split()

while "Season" not in command:
    fight = False

    if "->" in command:
        name = command[0]
        position = command[2]
        points = int(command[4])
        if name in player_pool:
            have_pos = False
            for i in range(len(player_pool[name])):
                pos = player_pool[name][i][0]
                if pos == position:
                    have_pos = True
                    old_points = player_pool[name][i][1]
                    if old_points < points:
                        player_pool[name][i][1] = points
                        break
            if not have_pos:
                player_pool[name].append([position, points])
        else:
            player_pool[name] = []
            player_pool[name].append([position, points])
    else:
        player_1 = command[0]
        player_2 = command[2]
        if player_1 in player_pool and player_2 in player_pool:
            total_1 = 0
            total_2 = 0
            for i_1 in player_pool[player_1]:
                position_1 = i_1[0]
                points_1 = i_1[1]
                for i_2 in player_pool[player_2]:
                    position_2 = i_2[0]
                    points_2 = i_2[1]
                    if position_1 == position_2:
                        total_1 += points_1
                        total_2 += points_2
                        break
            if total_1 > total_2:
                del player_pool[player_2]
            elif total_1 < total_2:
                del player_pool[player_1]

    command = input().split()

for player in player_pool:
    total_points = 0
    for info in player_pool[player]:
        points = info[1]
        total_points += points
    player_total[player] = total_points

player_total = dict(sorted(player_total.items(), key=lambda x: (-x[1], x[0])))

for player in player_total:
    print(f"{player}: {player_total[player]} skill")
    sorted_skills = sorted(player_pool[player], key=lambda x: (-x[1], x[0]))
    for info in sorted_skills:
        print(f"- {info[0]} <::> {info[1]}")
