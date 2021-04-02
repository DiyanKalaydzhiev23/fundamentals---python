price_bf_tax = 0

while True:
    part_price = input()
    if part_price == "special" or part_price == "regular":
        if price_bf_tax == 0:
            print(f"Invalid order!")
            break
        price = price_bf_tax
        taxes = price * 0.20
        price += taxes
        if part_price == "special":
            price *= 0.90
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_bf_tax:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {price:.2f}$")
        break
    part_price = float(part_price)
    if part_price <= 0:
        print("Invalid price!")
        continue
    price_bf_tax += part_price
