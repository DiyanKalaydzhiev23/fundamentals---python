import re

pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for _ in range(int(input())):
    match = re.findall(pattern, input())
    if match:
        match = ''.join(match)
        group = re.findall(r"\d", match)
        if group:
            print(f"Product group: {''.join(group)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
