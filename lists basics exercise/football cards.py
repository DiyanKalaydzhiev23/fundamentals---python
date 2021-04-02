cards = input().split()
a_team_counter = 11
b_team_counter = 11
removed_players = []
terminated = False
for el in cards:
    if "A" in el:
        if el in removed_players:
            continue
        else:
            removed_players.append(el)
            a_team_counter -= 1
    elif "B" in el:
        if el in removed_players:
            continue
        else:
            removed_players.append(el)
            b_team_counter -= 1
    if a_team_counter < 7 or b_team_counter < 7:
        print(f"Team A - {a_team_counter}; Team B - {b_team_counter}")
        terminated = True
        print("Game was terminated")
        break
if not terminated:
    print(f"Team A - {a_team_counter}; Team B - {b_team_counter}")
