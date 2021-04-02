data = [word.lower() for word in input().split()]
odd_dict = {}

for word in data:
    if word in odd_dict:
        odd_dict[word] += 1
    else:
        odd_dict[word] = 1

for word, value in odd_dict.items():
    if odd_dict[word] % 2 != 0:
        print(word, end=" ")
