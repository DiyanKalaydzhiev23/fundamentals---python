command = input()
coffee = 0
extra_sleep = False
while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee += 2
    if coffee > 5:
        print("You need extra sleep")
        extra_sleep = True
        break
    command = input()
if not extra_sleep:
    print(coffee)
