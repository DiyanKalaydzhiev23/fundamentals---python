products = [el for el in input().split()]
my_dict = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i+1]
    my_dict[key] = int(value)

check_products = input().split()

for product in check_products:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
