type_input = input()
symbol = input()


def int_type(num):
    number = int(num)
    result = number * 2
    print(result)


def real_type(num):
    number = float(num)
    result = number * 1.5
    print(f"{result:.2f}")


def string_type(text):
    string = "$" + text + "$"
    print(string)


if type_input == "int":
    int_type(symbol)
elif type_input == "real":
    real_type(symbol)
else:
    string_type(symbol)
