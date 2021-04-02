import re

valid_emails = []
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"
[valid_emails.append(el.group()) for el in re.finditer(pattern, input())]
[print(email) for email in valid_emails]
