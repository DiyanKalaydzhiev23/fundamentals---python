import re

participants = input().split(", ")

pattern = r"[a-zA-Z0-9]"
text = input()
names_dict = {}
places = ["1st place:", "2nd place:", "3rd place:"]

while text != "end of race":
    name = []
    km = 0

    for el in re.findall(pattern, text):
        if str(el).isalpha():
            name.append(el)
        elif str(el).isdigit():
            km += int(el)
    name = "".join(name)

    if name in participants:
        if name in names_dict:
            names_dict[name] += km
        else:
            names_dict[name] = km

    text = input()

sorted_players = sorted(names_dict.items(), key=lambda x: -x[1])
[print(f"{places[i]} {sorted_players[i][0]}") for i in range(3)]
