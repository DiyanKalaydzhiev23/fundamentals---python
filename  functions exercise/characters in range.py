first = input()
last = input()


def between():
    num1 = ord(first)
    num2 = ord(last)
    for number in range(num1 + 1, num2):
        print(chr(number), end=" ")


between()
