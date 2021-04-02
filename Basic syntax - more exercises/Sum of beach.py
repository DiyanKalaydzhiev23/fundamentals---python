word = input()
word = word.lower()
counter = 0
for i in range(0, len(word)):
    if i == len(word) - 1:
        break
    if word[i] == 's' and word[i + 1] == 'u' and word[i + 2] == 'n':
        counter += 1
    elif word[i] == 'f' and word[i + 1] == 'i' and word[i + 2] == 's' and word[i + 3] == 'h':
        counter += 1
    elif word[i] == 's' and word[i + 1] == 'a' and word[i + 2] == 'n' and word[i + 3] == 'd':
        counter += 1
    elif word[i] == 'w' and word[i + 1] == 'a' and word[i + 2] == 't' and word[i + 3] == 'e' and word[i + 4] == 'r':
        counter += 1
print(counter)
