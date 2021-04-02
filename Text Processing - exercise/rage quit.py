text = list(input())
ready_text = []
symbols_used = []
current_text = []
i = 0

while i < len(text):
    number = []
    if not text[i].isdigit():
        current_text.append(text[i])
        symbols_used.append(str(text[i]).upper())
        index = i + 1
        while len(text) > index and text[index].isdigit():
            number.append(text[index])
            index += 1
            i += 1
        if number:
            current_text = ''.join(current_text)
            current_text = current_text.upper()
            number = int(''.join(number))
            ready_text.append(current_text*number)
            current_text = []
    i += 1

symbols_used = set(symbols_used)
print(f"Unique symbols used: {len(symbols_used)}")
print(''.join(ready_text))
