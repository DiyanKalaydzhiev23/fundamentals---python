lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
money_repair = 0
shield_breaks = False
counter_shield_breaks = 0
for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        money_repair += helmet_price
    if i % 3 == 0:
        money_repair += sword_price
        if i % 2 == 0:
            shield_breaks = True
            counter_shield_breaks += 1
    if shield_breaks:
        money_repair += shield_price
    if counter_shield_breaks == 2:
        money_repair += armor_price
        counter_shield_breaks = 0
    shield_breaks = False
print(f"Gladiator expenses: {money_repair:.2f} aureus")
