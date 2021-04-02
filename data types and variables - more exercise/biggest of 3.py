import sys
max_num = -sys.maxsize
for i in range(3):
    num = int(input())
    if num > max_num:
        max_num = num
print(max_num)
