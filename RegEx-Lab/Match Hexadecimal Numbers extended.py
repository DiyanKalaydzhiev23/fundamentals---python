import re

pattern = r"\b(?:0x)?[0-9A-F]+\b"
[print(num, end=" ") for num in re.findall(pattern, input())]
