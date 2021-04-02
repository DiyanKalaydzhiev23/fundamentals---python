info = input().split()
base = int(info[0])
num = int(info[1])
result = []

while num > 0:
    n = num % base
    result.append(str(n))
    num //= base

print(''.join(result[::-1]))
