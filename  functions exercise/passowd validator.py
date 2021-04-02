password = input().lower()


def check():
    length = False
    only = False
    min_digits = False
    counter_digits = 0
    if 6 <= len(password) <= 10:
        length = True
    for letter in password:
        if 48 <= ord(letter) <= 57:
            only = True
        elif 97 <= ord(letter) <= 122:
            only = True
        else:
            only = False
            break
    for letter in password:
        if 48 <= ord(letter) <= 57:
            counter_digits += 1
    if counter_digits >= 2:
        min_digits = True
    if not length:
        print("Password must be between 6 and 10 characters")
    if not only:
        print("Password must consist only of letters and digits")
    if not min_digits:
        print("Password must have at least 2 digits")
    if length and only and min_digits:
        print("Password is valid")


check()
