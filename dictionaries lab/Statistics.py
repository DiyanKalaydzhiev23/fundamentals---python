command = input().split(": ")
products = {}

while "statistics" not in command:
    key = command[0]
    value = command[1]
    if key in products:
        products[key] += int(value)
    else:
        products[key] = int(value)
    command = input().split(": ")

print("Products in stock:")

[print(f"- {product}: {quantity}") for product, quantity in products.items()]
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
