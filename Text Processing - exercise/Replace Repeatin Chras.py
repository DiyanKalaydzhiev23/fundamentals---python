word = input()
ready_word = []

for i in range(len(word)):
    if i == 0:
        ready_word.append(word[i])
    elif ready_word[-1] != word[i]:
        ready_word.append(word[i])

print(f"{''.join(ready_word)}")
