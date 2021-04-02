dwarfs = {}
data = input().split(" <:> ")

while "Once upon a time" not in data:
    name = data[0]
    color = data[1]
    physics = int(data[2])
    already_in = False

    if color in dwarfs:
        for i in range(len(dwarfs[color])):
            dwarf_name = dwarfs[color][i][0]
            if name == dwarf_name:
                dwarf_physics = dwarfs[color][i][1]
                already_in = True
                if dwarf_physics < physics:
                    dwarfs[color][i][1] = physics
        if not already_in:
            dwarfs[color].append([name, physics])
    else:
        dwarfs[color] = []
        dwarfs[color].append([name, physics])

    data = input().split(" <:> ")

dwarfs = 
print(dwarfs)
