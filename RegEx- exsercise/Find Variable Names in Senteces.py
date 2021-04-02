import re

pattern = r"((?<=\s_)|(?<=^_))[a-zA-Z0-9]+((?=\s)|(?=$))"
valid = []
result = [valid.append(el.group()) for el in re.finditer(pattern, input())]
print(*valid, sep=",")
