numbers = [int(el) for el in input().split()]
text = input()

while text != "find":
    text = list(text)
    i_numbers = 0
    started = False
    type_treasure = []
    location = []

    for i_text in range(len(text)):
        current_letter = ord(text[i_text])
        current_letter -= numbers[i_numbers]
        text[i_text] = chr(current_letter)
        i_numbers += 1
        if i_numbers == len(numbers):
            i_numbers = 0

    for el in text:
        if el == '&' and started:
            started = False
        elif el == '&':
            started = True
        elif started:
            type_treasure.append(el)

    for el in text:
        if el == "<":
            started = True
        elif el == ">":
            started = False
        elif started:
            location.append(el)

    print(f"Found {''.join(type_treasure)} at {''.join(location)}")
    text = input()
