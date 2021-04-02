import re
text = input()
pattern = fr"\b{input()}\b"
print(len(re.findall(pattern, text, re.IGNORECASE)))
