numbers = input().split(", ")


def palindrome():
    for i in range(len(numbers)):
        current = numbers[i]
        reversed_num = current[::-1]
        if reversed_num == current:
            print(True)
        else:
            print(False)


palindrome()
