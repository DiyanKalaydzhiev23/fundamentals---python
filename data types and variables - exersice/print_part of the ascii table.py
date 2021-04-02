start = int(input())
end = int(input())
symbol = ""
for i in range(start, end + 1):
    symbol = chr(i)
    print(symbol, end=" ")
