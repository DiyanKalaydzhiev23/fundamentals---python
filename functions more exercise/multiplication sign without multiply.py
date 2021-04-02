num1 = int(input())
num2 = int(input())
num3 = int(input())
counter_negative = 0

if num1 < 0:
    counter_negative += 1
if num2 < 0:
    counter_negative += 1
if num3 < 0:
    counter_negative += 1

if num1 == 0 or num2 == 0 or num3 == 0:
    print("zero")
elif counter_negative == 1 or counter_negative == 3:
    print("negative")
else:
    print("positive")
