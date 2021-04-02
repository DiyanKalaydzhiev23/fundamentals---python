number = int(input())
is_prime = False
for i in range(2, number):
    if number % i == 0:
        print("False")
        is_prime = False
        break
    else:
        is_prime = True
if is_prime:
    print("True")
