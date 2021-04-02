import re

decrypt_pattern = r"[star]"
pattern = r"[^@\-\!:>]*?@(?P<name>[A-Z-a-z]+)[^@\-\!:>]*?:(?P<population>\d+)[^@\-\!:>]*?!(?P<attack>A|D)![^@\-\!:>]*?->(?P<count>\d+)[^@\-\!:>]*?"

n = int(input())
info = {'A': 0, 'D': 0}
planets = {'A': [], 'D': []}

for i in range(n):
    text = input()
    found = len(re.findall(decrypt_pattern, text, re.IGNORECASE))
    text = list(text)

    for j in range(len(list(text))):
        text[j] = chr(ord(text[j])-found)

    text = ''.join(text)
    result = re.finditer(pattern, text)
    for el in result:
        match = el.groupdict()
        if match['attack'] == "A":
            info['A'] += 1
            planets['A'].append(match['name'])
        else:
            info['D'] += 1
            planets['D'].append(match['name'])

print(f"Attacked planets: {info['A']}")
sorted_planets = sorted(planets['A'])
[print(f"-> {planet}") for planet in sorted_planets]
print(f"Destroyed planets: {info['D']}")
sorted_planets = sorted(planets['D'])
[print(f"-> {planet}") for planet in sorted_planets]
