number = int(input())


def count_sheep():
    print(" sheep...", end="")


for i in range(1, number + 1):
    print(i, end="")
    count_sheep()
