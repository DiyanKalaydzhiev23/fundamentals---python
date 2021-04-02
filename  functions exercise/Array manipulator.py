import sys
array = input().split()


def exchange(index):
    global array
    new_array = []
    max_index_array = len(array)
    if index > max_index_array - 1 or index < 0:
        print("Invalid index")
    else:
        for i in range(index+1, max_index_array):
            new_array.append(array[i])
        for i in range(index+1):
            new_array.append(array[i])
        array = new_array


def max_even_odd(type_num):
    even = False
    odd = False
    max_num = -sys.maxsize
    max_index = -1
    if type_num == "even":
        even = True
    else:
        odd = True
    for i in range(len(array)):
        if odd:
            if int(array[i]) % 2 != 0:
                if max_num <= int(array[i]):
                    max_num = int(array[i])
                    max_index = i
        else:
            if int(array[i]) % 2 == 0:
                if max_num <= int(array[i]):
                    max_num = int(array[i])
                    max_index = i
    if max_index == -1:
        print("No matches")
    else:
        print(max_index)


def min_even_odd(type_num):
    even = False
    odd = False
    min_num = sys.maxsize
    min_index = -1
    if type_num == "even":
        even = True
    else:
        odd = True
    for i in range(len(array)):
        if odd:
            if int(array[i]) % 2 != 0:
                if min_num >= int(array[i]):
                    min_num = int(array[i])
                    min_index = i
        else:
            if int(array[i]) % 2 == 0:
                if min_num >= int(array[i]):
                    min_num = int(array[i])
                    min_index = i
    if min_index == -1:
        print("No matches")
    else:
        print(min_index)


def first_even_odd(count, type_num):
    even = False
    odd = False
    count_more = False
    satisfied = False
    counter = 0
    numbers = []
    if type_num == "even":
        even = True
    elif type_num == "odd":
        odd = True
    if count > len(array):
        print("Invalid count")
        count_more = True
    else:
        for EL in array:
            if even:
                if int(EL) % 2 == 0:
                    numbers.append(int(EL))
                    counter += 1
                if counter == count:
                    print(numbers)
                    satisfied = True
                    break
            elif odd:
                if int(EL) % 2 != 0:
                    numbers.append(int(EL))
                    counter += 1
                if counter == count:
                    print(numbers)
                    satisfied = True
                    break
    if not satisfied and not count_more:
        print(numbers)


def last_even_odd(count, type_num):
    new_array = array[::-1]
    count_more = False
    even = False
    odd = False
    satisfied = False
    counter = 0
    numbers = []
    if type_num == "even":
        even = True
    elif type_num == "odd":
        odd = True
    if count > len(array):
        print("Invalid count")
        count_more = True
    else:
        for EL in new_array:
            if even:
                if int(EL) % 2 == 0:
                    numbers.append(int(EL))
                    counter += 1
                if counter == count:
                    numbers = numbers[::-1]
                    print(numbers)
                    satisfied = True
                    break
            elif odd:
                if int(EL) % 2 != 0:
                    numbers.append(int(EL))
                    counter += 1
                if counter == count:
                    numbers = numbers[::-1]
                    print(numbers)
                    satisfied = True
                    break
    if not satisfied and not count_more:
        numbers = numbers[::-1]
        print(numbers)


command = input().split()

while not "end" in command:
    if "exchange" in command:
        exchange(int(command[1]))
    elif "max" in command:
        max_even_odd(command[1])
    elif "min" in command:
        min_even_odd(command[1])
    elif "first" in command:
        first_even_odd(int(command[1]), command[2])
    elif "last" in command:
        last_even_odd(int(command[1]), command[2])
    command = input().split()

new_array_out = []

for el in array:
    element = int(el)
    new_array_out.append(element)

print(new_array_out)
