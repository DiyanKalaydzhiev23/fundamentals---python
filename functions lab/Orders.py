product = input()
times = int(input())

coffee = 1.50
water = 1
coke = 1.40
snacks = 2


def order():
    price = 0
    if product == "coffee":
        price = coffee * times
    elif product == "water":
        price = times * water
    elif product == "coke":
        price = times * coke
    elif product == "snacks":
        price = times * snacks
    return price


print(f"{order():.2f}")
