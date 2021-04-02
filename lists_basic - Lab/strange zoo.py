tail = input()
body = input()
head = input()
list_animal = [tail, body, head]
list_animal[0], list_animal[2] = list_animal[2], list_animal[0]
print(list_animal)
