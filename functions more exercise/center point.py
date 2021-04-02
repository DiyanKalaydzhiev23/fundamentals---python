import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def closest_check():
    global x1, x2, y1, y2
    p1 = math.sqrt(x1**2 + y1**2)
    p2 = math.sqrt(x2**2 + y2**2)
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    if p1 <= p2:
        print(f"({x1}, {y1})")
    else:
        print(f"({x2}, {y2})")


closest_check()
