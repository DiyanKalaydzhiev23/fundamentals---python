num = float(input())
if num == 0:
    print("zero")
elif abs(num) < 1:
    print("small", end=" ")
elif abs(num) > 1000000:
    print("large", end=" ")
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
