year = int(input())
next_year = year
list_used_numbers = list([])
next_happy_year = ""
is_used = False
while len(str(year)) != len(str(next_happy_year)):
    next_year += 1
    for index, value in enumerate(str(next_year)):
        if value in list_used_numbers:
            is_used = True
            break
        else:
            list_used_numbers += value
            next_happy_year += value
    if len(str(year)) == len(next_happy_year):
        print(next_happy_year)
        break
    else:
        list_used_numbers = list([])
        next_happy_year = ""
        is_used = False