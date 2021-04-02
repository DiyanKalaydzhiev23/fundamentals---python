animals = input().split(", ")
if animals.pop() == "wolf":
    print("Please go away and stop eating my sheep")
    raise SystemExit
animals_reversed = animals[::-1]
for i in range(len(animals_reversed)):
    if animals_reversed[i] != "sheep":
        print(f"Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!")
