import re

pattern = r'%(?P<name>[A-Z][a-z]+)%[^%\|\.\$]*<(?P<product>\w+)>[^%\|\.\$]*\|(?P<quantity>\d+)\|[^%\|\.\$]*?(?P<price>\d+(\.(\d+))?)\$'
text = input()
total_income = 0

while text != "end of shift":
    match = re.match(pattern, text)
    if match:
        data = match.groupdict()
        total_income += int(data['quantity'])*float(data['price'])
        print(f"{data['name']}: {data['product']} - {int(data['quantity'])*float(data['price']):.2f}")
    text = input()

print(f"Total income: {total_income:.2f}")
