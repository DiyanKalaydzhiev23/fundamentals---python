battlefield = input().split(">")
cleaned = []
explosion = 0

for el in battlefield:
    if el[0].isdigit():
        explosion += int(el[0])
        if len(el) <= explosion:
            explosion -= len(el)
            el = ">"
        else:
            el = ">" + "".join(list(el[explosion::]))
            explosion = 0
    cleaned.append(el)
print(f"{''.join(cleaned)}")
