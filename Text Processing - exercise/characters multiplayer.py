words = input().split()
word_1 = words[0]
word_2 = words[1]
result = 0

for i in range(len(word_1)):
    if word_1 and word_2:
        char_1 = ord(word_1[0])
        char_2 = ord(word_2[0])
        word_1 = word_1.replace(word_1[0], "", 1)
        word_2 = word_2.replace(word_2[0], "", 1)
        result += char_1 * char_2
    else:
        break

while word_1 or word_2:
    if word_1:
        char_1 = ord(word_1[0])
        word_1 = word_1.replace(word_1[0], "", 1)
    else:
        char_1 = ord(word_2[0])
        word_2 = word_2.replace(word_2[0], "", 1)
    result += char_1

print(result)
