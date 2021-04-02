n = int(input())
database = {}

for _ in range(n):
    command = input().split()
    type_command = command[0]
    username = command[1]

    if type_command == "register":
        license_plate = command[2]

        if username in database:
            print(f"ERROR: already registered with plate number {database[username]}")
        else:
            database[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    else:
        if username in database:
            database.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

[print(f"{user} => {plate}") for user, plate in database.items()]
