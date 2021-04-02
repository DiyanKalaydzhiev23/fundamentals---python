import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def longer():
    global x1, x2, y1, y2, x3, y3, x4, y4
    p1 = math.sqrt(x1**2 + y1**2)
    p2 = math.sqrt(x2**2 + y2**2)
    p3 = math.sqrt(x3**2 + y3**2)
    p4 = math.sqrt(x4**2 + y4**2)
    x1 = math.floor(x1)
    y1 = math.floor(y1)
    x2 = math.floor(x2)
    y2 = math.floor(y2)
    x3 = math.floor(x3)
    y3 = math.floor(y3)
    x4 = math.floor(x4)
    y4 = math.floor(y4)
    list_points = [p1, p2, p3, p4]
    longest_x1 = 0
    longest_y1 = 0
    longest_y2 = 0
    longest_x2 = 0
    max_point1 = 0
    max_point2 = 0
    for i in range(4):
        point = list_points[i]
        if point > max_point1:
            max_point1 = point
    list_points.remove(max_point1)
    if max_point1 == p1:
        longest_x1 = x1
        longest_y1 = y1
        p1 = -1
    elif max_point1 == p2:
        longest_x1 = x2
        longest_y1 = y2
        p2 = -1
    elif max_point1 == p3:
        longest_x1 = x3
        longest_y1 = y3
        p3 = -1
    elif max_point1 == p4:
        longest_x1 = x4
        longest_y1 = y4
        p4 = -1
    for i in range(3):
        point = list_points[i]
        if point > max_point2:
            max_point2 = point
    if max_point2 == p1:
        longest_x2 = x1
        longest_y2 = y1
    elif max_point2 == p2:
        longest_x2 = x2
        longest_y2 = y2
    elif max_point2 == p3:
        longest_x2 = x3
        longest_y2 = y3
    elif max_point2 == p4:
        longest_x2 = x4
        longest_y2 = y4
    c1 = math.sqrt(longest_x1**2 + longest_y1**2)
    c2 = math.sqrt(longest_x2**2 + longest_y2**2)
    if c1 <= c2:
        print(f"({longest_x1}, {longest_y1})({longest_x2}, {longest_y2})")
    else:
        print(f"({longest_x2}, {longest_y2})({longest_x1}, {longest_y1})")


longer()
