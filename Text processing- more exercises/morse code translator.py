dictionary = {'.-': "A", '-...': "B", '-.-.': "C",
              '-..': "D", '.': "E", '..-.': "F", '--.': "G",
              '....': "H", '..': "I", '.---': "J", '-.-': "K",
              '.-..': "L", '--': "M", '-.': "N", '---': "O",
              '.--.': "P", '--.-': "Q", '.-.': "R", '...': "S",
              '-': "T", '..-': "U", '...-': "V", '.--': "W",
              '-..-': "X", '-.--': "Y", '--..': "Z"}

text = input().split("|")

for el in text:
    el = el.strip()
    letters = el.split(" ")
    for letter in letters:
        print(dictionary[letter], end="")
    print(" ", end="")
