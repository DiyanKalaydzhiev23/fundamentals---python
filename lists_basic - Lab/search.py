n = int(input())
word = input()
text_list = []
match_text_list = []
for words in range(n):
    text = input()
    text_list.append(text)
    if word in text:
        match_text_list.append(text)
print(text_list)
print(match_text_list)
