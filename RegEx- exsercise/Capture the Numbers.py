import re

pattern = r"\d+"
text = input()

while text:
    [print(el, end=" ") for el in re.findall(pattern, text)]
    text = input()
