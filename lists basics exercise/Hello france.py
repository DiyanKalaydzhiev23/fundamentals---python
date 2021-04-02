items = input().split("|")
budget = float(input())
profit_list = []
sold = 0
profit = 0
for i in range(len(items)):
    new_price = 0
    item = items.pop(0).split("->")
    if float(item[1]) <= budget:
        if item[0] == "Clothes" and float(item[1]) <= 50:
            budget -= float(item[1])
            new_price = float(item[1]) * 1.40
            sold += new_price
            profit_list.append(str(new_price))
            profit += (new_price - float(item[1]))
        elif item[0] == "Shoes" and float(item[1]) <= 35:
            budget -= float(item[1])
            new_price = float(item[1]) * 1.40
            sold += new_price
            profit_list.append(str(new_price))
            profit += (new_price - float(item[1]))
        elif item[0] == "Accessories" and float(item[1]) <= 20.50:
            budget -= float(item[1])
            new_price = float(item[1]) * 1.40
            sold += new_price
            profit_list.append(str(new_price))
            profit += (new_price - float(item[1]))
for i in range(len(profit_list)):
    el = profit_list[i]
    if i != len(profit_list) - 1:
        print(f"{float(el):.2f}", end=" ")
    else:
        print(f"{float(el):.2f}")
total_money = budget + sold
print(f"Profit: {profit:.2f}")
if total_money >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
