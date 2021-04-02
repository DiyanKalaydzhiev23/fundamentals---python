num = int(input())
sum_chr = 0
for i in range(1, num + 1):
    symbol = input()
    sum_chr += ord(symbol)
print(f"The sum equals: {sum_chr}")
