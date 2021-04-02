num1 = int(input())
num2 = int(input())


def factor_first():
    factor_one = 1
    for num in range(1, num1 + 1):
        factor_one *= num
    return factor_one


def factor_second():
    factor_two = 1
    for num in range(1, num2 + 1):
        factor_two *= num
    return factor_two


def divide():
    result = factor_first() / factor_second()
    print(f"{result:.2f}")


divide()
