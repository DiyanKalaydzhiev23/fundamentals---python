cars = {}

for _ in range(int(input())):
    tokens = input().split("|")
    cars[tokens[0]] = [int(tokens[1]), int(tokens[2])]

command = input().split(" : ")

while command[0] != "Stop":
    if command[0] == "Drive":
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[command[1]][0] > 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif command[0] == "Refuel":
        car, fuel = command[1], int(command[2])
        if cars[car][1] + fuel > 75:
            fuel = 75 - cars[car][1]
        cars[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
    elif command[0] == "Revert":
        car, kilometers = command[1], int(command[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input().split(" : ")

cars = dict(sorted(cars.items(), key=lambda x: (-x[1][0], x[0])))
[print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.") for car in cars]
