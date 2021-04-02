import re

pattern = r"<a.+>"
line = input()

while line != "end":
    if "</a>" in line:
        line = line.replace("</a>", "[/URL]")
    if '<a' in line:
        part = ''.join(re.findall(pattern, line))
        found = part
        found = found.replace("<a", "[URL")
        found = found.replace(">", "]")
        line = line.replace(part, found)
    print(line)
    line = input()
