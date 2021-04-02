for name in input().split(", "):
    current_username = name
    after_digits = []
    if 3 < len(name) < 16:
        while "-" in name or "_" in name:
            name = name.replace("-", "")
            name = name.replace("_", "")
        [after_digits.append(letter) for letter in name if not letter.isdigit()]
        name = f"{''.join(after_digits)}"
        if name.isalpha():
            print(current_username)
