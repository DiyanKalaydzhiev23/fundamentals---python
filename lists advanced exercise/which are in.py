substrings = input().split(", ")
words = input().split(", ")
are_in = []

for substring in substrings:
    for word in words:
        if substring in word:
            are_in.append(substring)
            break

print(are_in)
