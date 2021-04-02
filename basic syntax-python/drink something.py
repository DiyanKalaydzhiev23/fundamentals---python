age = int(input())


def drinks(drink):
    print(f"drink {drink}")


if age <= 14:
    drinks("toddy")
elif age <= 18:
    drinks("coke")
elif age <= 21:
    drinks("beer")
else:
    drinks("whisky")
