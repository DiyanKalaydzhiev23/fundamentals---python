import re
pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"
numbers = input()
result = re.finditer(pattern, numbers)
print(", ".join([str(el.group()) for el in result]))
