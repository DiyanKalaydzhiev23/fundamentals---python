def check_for_empty():
    there_are = False
    for el in seats:
        if el < 4:
            there_are = True
            break
    return there_are


people = int(input())
seats = [int(el) for el in input().split()]

while True:

    for i in range(len(seats)):
        if seats[i] < 4:
            free_space = 4 - seats[i]
            if free_space > people:
                seats[i] += people
                people = 0
            else:
                seats[i] += free_space
                people -= free_space

    is_empty = check_for_empty()

    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!\n{' '.join(list(map(lambda x: str(x), seats)))}")
    elif people == 0 and is_empty:
        print(f"The lift has empty spots!\n{' '.join(list(map(lambda x: str(x), seats)))}")
    else:
        print(f"{' '.join(list(map(lambda x: str(x), seats)))}")
    break
