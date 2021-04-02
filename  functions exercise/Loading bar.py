num = int(input())


def load():
    is_load = num // 10
    not_load = 10 - is_load
    percent = "%"
    dot = "."
    if num != 100:
        print(f"{num}% [{is_load * percent}{not_load * dot}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{10 * percent}]")


load()
