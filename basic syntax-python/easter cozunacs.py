budget = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = 1.25 * price_flour
cozunacs_made = 0
one_cozunac = price_eggs + price_flour + (price_milk / 4)
colored_eggs = 0
while True:
    budget -= one_cozunac
    cozunacs_made += 1
    colored_eggs += 3
    if cozunacs_made % 3 == 0:
        colored_eggs -= (cozunacs_made - 2)
    if budget - one_cozunac < 0:
        break
print(f"You made {cozunacs_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
