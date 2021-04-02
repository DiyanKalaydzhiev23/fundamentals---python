num = int(input())
capacity = 255
for i in range(num):
    liters = int(input())
    if capacity - liters < 0:
        print("Insufficient capacity!")
    else:
        capacity -= liters
print(f"{255 - capacity}")
