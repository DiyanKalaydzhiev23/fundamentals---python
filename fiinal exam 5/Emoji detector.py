import re

text = input()
pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"
numbers = [int(num) for num in re.findall(r"\d", text)]
cool_threshold = 1

for el in numbers:
    cool_threshold *= int(el)

match = re.findall(pattern, text)
print(f"Cool threshold: {cool_threshold}")

if match:
    print(f"{len(match)} emojis found in the text. The cool ones are:")
    for el in match:
        coolness = 0
        for letter in el[1]:
            coolness += ord(letter)
        if coolness >= cool_threshold:
            print(''.join(el[0] + el[1] + el[2]))
