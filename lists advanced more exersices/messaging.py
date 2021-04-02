numbers = input().split()
text = [value for index, value in enumerate(input())]
decrypted = ""

for num in range(len(numbers)):
    num_letter = numbers[num]
    index_sum = 0
    for index, value in enumerate(num_letter):
        index_sum += int(value)
    if index_sum > len(text)-1:
        while index_sum >= len(text):
            index_sum -= len(text)
    decrypted += text[index_sum]
    text.pop(index_sum)

print(decrypted)
