text = input().split()
first = [ord(el) for el in text[0]]
second = [ord(el) for el in text[1]]
print(sum(first)*sum(second))
