text = input().split()
max_index = len(text) - 1
half_index = int(len(text) / 2)
side_a = []
side_b = []
num = int(input())
for i in range(0, half_index):
    side_a.append(text[i])
for i in range(half_index, max_index + 1):
    side_b.append(text[i])
for i in range(1, num + 1):
    current_list = [side_a[0]]
    for index in range(1, half_index):
        current_list.append(side_b[index - 1])
        current_list.append(side_a[index])
    current_list.append(side_b[-1])
    text = current_list
    side_a = []
    side_b = []
    for j in range(0, half_index):
        side_a.append(text[j])
    for j in range(half_index, max_index + 1):
        side_b.append(text[j])
print(text)
