todo = ["0" for iter in range(11)]
command = input().split("-")

while "End" not in command:
    index = int(command[0])
    task = command[1]
    todo[index] = task
    command = input().split("-")

new_todo = []

for el in todo:
    if el != "0":
        new_todo.append(el)

print(new_todo)
