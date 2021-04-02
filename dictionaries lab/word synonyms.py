n = int(input())
dictionary = {}

for i in range(n):
    word = input()
    synonym = input()
    if word in dictionary:
        dictionary[word] += ", " + synonym
    else:
        dictionary[word] = synonym

[print(f"{word} - {synonym}") for word, synonym in dictionary.items()]
