first_str = input()
second_str = input()
changed_word = ""
current_word = ""
word_exists = False
length_of_word = len(first_str)
while True:
    for index, value in enumerate(second_str):
        changed_word += value
        current_word += changed_word
        for ind, val in enumerate(first_str):
            if index == ind and val == value:
                word_exists = True
                break
            if ind > index:
                current_word += val
        if not word_exists:
            print(current_word)
        if current_word == second_str:
            break
        current_word = ""
        word_exists = False
    break
