n = int(input())

for i in range(n):
    text = input()
    name = []
    age = []
    start_found = False
    for el in text:
        if el == "@":
            start_found = True
            continue
        elif el == "|":
            start_found = False
        if start_found:
            name.append(el)
    for el in text:
        if el == "#":
            start_found = True
            continue
        elif el == "*":
            start_found = False
        if start_found:
            age.append(el)

    print(f"{''.join(name)} is {''.join(age)} years old.")
