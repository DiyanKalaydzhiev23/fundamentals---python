atom = int(input())
shells = []
shell = 1

while atom > 0:
    max_electrons = 2*shell**2
    if atom - max_electrons > 0:
        shells.append(max_electrons)
        atom -= max_electrons
    else:
        shells.append(atom)
        atom -= atom
    shell += 1

print(shells)
