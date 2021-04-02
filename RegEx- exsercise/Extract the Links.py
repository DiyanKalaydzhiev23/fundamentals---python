import re

pattern = r"www.[a-zA-Z0-9-]+\.[a-z]+([\.a-z]+)+"
text = input()

while text:
    result = re.finditer(pattern, text)
    if result:
        [print(el.group()) for el in result]
    text = input()
