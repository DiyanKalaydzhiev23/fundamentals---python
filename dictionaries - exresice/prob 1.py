n = int(input())
total = 0

for _ in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    price = days * capsules_count * price_per_capsule
    total += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total:.2f}")
