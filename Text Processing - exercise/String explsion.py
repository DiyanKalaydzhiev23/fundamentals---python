battlefield = list(input())
ready_word = []
i = 0

while i < len(battlefield):
    if battlefield[i] == ">":
        if not str(battlefield[i+1]).isdigit():
            i += 1
            continue

    if battlefield[i] == ">":
        explosion_range = int(battlefield[i+1])
        battlefield.pop(i+1)
        j = 1
        rolled = False

        while explosion_range > j:
            if battlefield[i+j] == ">":
                explosion_range += int(battlefield[i+j+1])
                battlefield.pop(i+j+1)
                j += 1
            else:
                battlefield.pop(j+i)
                explosion_range -= 1
            rolled = True
        if rolled:
            i += 1
    i += 1

print(f"{''.join(battlefield)}")
