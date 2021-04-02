product_data = input().split()
products = {}

while "buy" not in product_data:
    product = product_data[0]
    price = float(product_data[1])
    quantity = int(product_data[2])

    if product not in products:
        products[product] = []
        products[product].append(price)
        products[product].append(quantity)
    else:
        products[product][0] = price
        products[product][1] += quantity

    product_data = input().split()

[print(f"{product} -> {data[0] * data[1]:.2f}") for product, data in products.items()]
