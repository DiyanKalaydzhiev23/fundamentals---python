import re

pattern = r"(=|/)([A-Z][a-zA-Z][A-za-z]+)\1"
destinations = [el.group(2) for el in re.finditer(pattern, input())]
points = 0

for el in destinations:
    points += len(el)

print(f"Destinations: {', '.join(destinations)}\nTravel Points: {points}")
