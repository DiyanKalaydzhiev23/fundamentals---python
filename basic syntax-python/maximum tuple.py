number = int(input())
max_number = int(input())
score = number
while score <= max_number:
    score += number
last_score = score - number
print(last_score)
