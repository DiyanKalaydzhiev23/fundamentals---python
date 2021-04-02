word = input()

nums = []
letters = []
others = []

for index, value in enumerate(word):
    if str(value).isdigit():
        nums.append(value)
    elif str(value).isalpha():
        letters.append(value)
    else:
        others.append(value)

print(f"{''.join(nums)}")
print(f"{''.join(letters)}")
print(f"{''.join(others)}")
