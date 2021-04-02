materials = {}
material = input()

while material != "stop":
    quantity = int(input())

    if material in materials:
        materials[material] += quantity
    else:
        materials[material] = quantity

    material = input()

[print(f"{material} -> {quantity}") for material, quantity in materials.items()]
