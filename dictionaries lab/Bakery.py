products = [el for el in input().split()]
my_dict = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i+1]
    my_dict[key] = int(value)

print(my_dict)
