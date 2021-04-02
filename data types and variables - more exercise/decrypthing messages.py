key = int(input())
num = int(input())
text = ""
for i in range(num):
    letter = input()
    letter_done = chr(ord(letter) + key)
    text += letter_done
print(text)
