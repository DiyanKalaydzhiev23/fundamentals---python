initial_sequence = input().split()
number = int(input())
permutation_list = []
result = ""
index = 0
while initial_sequence:
    index += number - 1
    while index >= len(initial_sequence):
        index = index - len(initial_sequence)
    kill = initial_sequence.pop(index)
    permutation_list.append(int(kill))
for i in range(len(permutation_list)):
    if i == 0:
        result += "[" + str(permutation_list[i])
    elif i == len(permutation_list) - 1:
        result += "," + str(permutation_list[i]) + "]"
    else:
        result += "," + str(permutation_list[i])
print(result)
