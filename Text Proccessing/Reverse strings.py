word = input()

while "end" not in word:
    print(f"{word} = {word[::-1]}")
    word = input()
