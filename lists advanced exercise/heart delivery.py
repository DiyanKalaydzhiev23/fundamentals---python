neighborhood = [int(house) for house in input().split("@")]

command = input().split()
house = 0

while "Love!" not in command:
    jump = int(command[1])
    if jump + house >= len(neighborhood):
        house = 0
    else:
        house += jump
    if neighborhood[house] == 0:
        print(f"Place {house} already had Valentine's day.")
    else:
        neighborhood[house] -= 2
        if neighborhood[house] == 0:
            print(f"Place {house} has Valentine's day.")
    command = input().split()

print(f"Cupid's last position was {house}.")
failed_houses = [house for house in neighborhood if house != 0]

if len(failed_houses) > 0:
    print(f"Cupid has failed {len(failed_houses)} places.")
else:
    print("Mission was successful.")
