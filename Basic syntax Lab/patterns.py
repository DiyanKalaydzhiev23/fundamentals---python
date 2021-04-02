num = int(input())
star = "*"
star_counter = 1
for i in range(num):
    print(star * star_counter)
    star_counter += 1
star_counter -= 2
for i in range(num):
    print(star_counter * star)
    star_counter -= 1
