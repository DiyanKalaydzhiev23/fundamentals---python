import sys
population = [int(human) for human in input().split(", ")]
min_wealth = int(input())
equal = False


def who_is_richest():
    richest_money = -sys.maxsize
    richest_index = None
    for human_money in population:
        if human_money > richest_money:
            richest_money = human_money
            richest_index = population.index(richest_money)
    return richest_index


def is_equal():
    it_is = False
    for el in population:
        if el < min_wealth:
            it_is = False
            break
        else:
            it_is = True
    return it_is


sum_of_population = 0

for money in population:
    sum_of_population += money

if sum_of_population / len(population) < min_wealth:
    print("No equal distribution possible")
    raise SystemExit

while not equal:
    rich_index = who_is_richest()
    for i in range(len(population)):
        if population[i] < min_wealth:
            difference = min_wealth - population[i]
            if population[rich_index] - difference < min_wealth:
                difference = (population[rich_index] - min_wealth)
                population[rich_index] -= difference
                population[i] += difference
                break
            population[rich_index] -= difference
            population[i] += difference
    equal = is_equal()

print(population)
