materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
obtained = False

while not obtained:
    elements = [el.lower() for el in input().split()]

    for i in range(0, len(elements), 2):
        quantity = int(elements[i])
        material = elements[i+1]

        if material == "motes" or material == "shards" or material == "fragments":
            materials[material] += quantity
            if materials[material] >= 250:
                result = ""
                if material == "shards":
                    result = "Shadowmourne"
                elif material == "fragments":
                    result = "Valanyr"
                elif material == "motes":
                    result = "Dragonwrath"
                print(f"{result} obtained!")
                materials[material] -= 250
                obtained = True
                break
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity

materials = dict(sorted(materials.items(), key=lambda x: (-x[1], x[0])))
junk = dict(sorted(junk.items(), key=lambda x: x[0]))

[print(f"{el}: {n}") for el, n in materials.items()]
[print(f"{el}: {n}") for el, n in junk.items()]
