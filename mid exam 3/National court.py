employer_1_hrs = int(input())
employer_2_hrs = int(input())
employer_3_hrs = int(input())
max_ppl_hrs = employer_1_hrs + employer_2_hrs + employer_3_hrs
people = int(input())
hours_needed = 0
times = 1

while people > 0:
    if times % 4 == 0:
        pass
    elif people <= max_ppl_hrs:
        people -= people
    else:
        people -= max_ppl_hrs
    hours_needed += 1
    times += 1

print(f"Time needed: {hours_needed}h.")
