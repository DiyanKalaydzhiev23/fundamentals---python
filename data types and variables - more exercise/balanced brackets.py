num = int(input())
first_bracket = False
second_bracket = False
balanced = False
for i in range(num):
    symbols = input()
    if symbols == "(":
        if first_bracket:
            break
        first_bracket = True
        balanced = False
    elif symbols == ")":
        second_bracket = True
        if not first_bracket:
            balanced = False
            break
        else:
            balanced = True
            first_bracket = False
            second_bracket = False
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
