text = list(input())

for i in range(len(text)):
    text[i] = chr(ord(text[i])+3)

print(f"{''.join(text)}")
