import re
pattern = r"\b(?P<Day>\d{2})(?P<separator>[\.\\/\-])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})\b"
date = input()
result = re.findall(pattern, date)
[print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}") for match in result]
