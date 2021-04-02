num = int(input())


def even_odd_sum():
    global num
    even_sum = 0
    odd_sum = 0
    while num > 0:
        current = num % 10
        num = num // 10
        if current % 2 == 0:
            even_sum += current
        else:
            odd_sum += current
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


even_odd_sum()
