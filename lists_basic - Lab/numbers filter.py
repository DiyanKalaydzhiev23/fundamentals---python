n = int(input())
total_list = []
criteria_list = []
for numbers in range(n):
    number = int(input())
    total_list.append(number)
criteria = input()
for numbers in total_list:
    if criteria == "even":
        if numbers == 0:
            criteria_list.append(numbers)
        elif numbers % 2 == 0:
            criteria_list.append(numbers)
    elif criteria == "odd":
        if numbers == 0:
            continue
        elif numbers % 2 != 0:
            criteria_list.append(numbers)
    elif criteria == "positive":
        if numbers >= 0:
            criteria_list.append(numbers)
    elif criteria == "negative":
        if numbers < 0:
            criteria_list.append(numbers)
print(criteria_list)
