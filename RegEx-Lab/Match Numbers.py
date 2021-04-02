import re
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
info = input()
result = re.finditer(pattern, info)
[print(match.group(0), end=" ") for match in result]
