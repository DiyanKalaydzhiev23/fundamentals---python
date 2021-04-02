all_words = input().split()
searching_word = input()
palindrome_words = [word for word in all_words if word[::-1] == word]
found_word = palindrome_words.count(searching_word)
print(palindrome_words)
print(f"Found palindrome {found_word} times")
