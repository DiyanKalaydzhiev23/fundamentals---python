num = int(input())


def check():
    sum_divisors = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_divisors += divisor
    if sum_divisors == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


check()
