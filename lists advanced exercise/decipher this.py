crypt_words = input().split()

for word in crypt_words:
    first_number = ""
    second_part = ""
    for letter in word:
        if 48 <= ord(letter) <= 57:
            first_number += letter
        else:
            second_part += letter
    first_letter = chr(int(first_number))
    half = first_letter + second_part
    current_list = [value for index, value in enumerate(half)]
    current_list[1], current_list[-1] = current_list[-1], current_list[1]
    print(''.join(current_list), end=" ")
