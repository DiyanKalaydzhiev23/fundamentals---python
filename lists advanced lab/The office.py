numbers = list(map(lambda x: int(x), input().split()))
factor = int(input())
numbers = [num*factor for num in numbers]
total_count = len(numbers)
total_sum = 0

for num in numbers:
    total_sum += num

average = total_sum / total_count
happy_list = [happy for happy in numbers if happy >= average]
print(f"Score: {len(happy_list)}/{total_count}.", end=" ")

if len(happy_list) >= int(total_count / 2):
    print("Employees are happy!")
else:
    print("Employees are not happy!")
