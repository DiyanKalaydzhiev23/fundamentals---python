operation = input()
num1 = int(input())
num2 = int(input())


def do_operation():
    if operation == "add":
        return num2 + num1
    elif operation == "subtract":
        return num1 - num2
    elif operation == "divide":
        return int(num1 / num2)
    elif operation == "multiply":
        return num1 * num2


print(do_operation())
