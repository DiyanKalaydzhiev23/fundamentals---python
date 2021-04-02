num = int(input())
for i in range(1, num + 1):
    sum_of_digits = 0
    digits = i
    while digits > 0:
        if digits >= 10:
            sum_of_digits += digits % 10
            digits = int(digits / 10)
        else:
            sum_of_digits += digits
            digits = 0
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
