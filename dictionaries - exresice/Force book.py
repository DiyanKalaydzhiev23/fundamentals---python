def check_command(type_command):
    result = False
    type_command = type_command.split()
    if "|" in type_command:
        result = True
    return result


command = input()
force_book = {}

while "Lumpawaroo" not in command:
    is_vertical = check_command(command)

    if is_vertical:
        command = command.split(" | ")
        command = command[::-1]
    else:
        command = command.split(" -> ")

    force_user = command[0]
    force_side = command[1]

    if is_vertical:
        if force_user not in force_book.values():
            if force_side not in force_book:
                force_book[force_side] = []
                force_book[force_side].append(force_user)
            force_book[force_side].append(force_user)
    else:
        other_key = ""
        for key in force_book:
            if key != force_side:
                other_key = key
                break
        if force_user in force_book[other_key]:
            force_book[other_key].remove(force_user)
            if force_side in force_book:
                force_book[force_side].append(force_user)
            else:
                force_book[force_side] = []
                force_book[force_side].append(force_user)
        else:
            if force_side in force_book:
                force_book[force_side].append(force_user)
            else:
                force_book[force_side] = []
                force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

force_book = dict(sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])))

for keys, value in force_book.items():
    force_book[keys] = list(sorted(force_book[keys]))

for key, value in force_book.items():
    if len(force_book[key]) == 0:
        continue
    else:
        print(f"Side: {key}, Members: {len(force_book[key])}")
        [print(f"! {name}") for name in force_book[key]]
