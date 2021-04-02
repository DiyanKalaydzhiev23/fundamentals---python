companies = {}
data = input().split(" -> ")

while "End" not in data:
    company_name = data[0]
    worker_id = data[1]

    if company_name not in companies:
        companies[company_name] = []
        companies[company_name].append(worker_id)
    else:
        if worker_id not in companies[company_name]:
            companies[company_name].append(worker_id)

    data = input().split(" -> ")

companies = dict(sorted(companies.items(), key= lambda x: x[0]))

for company in companies:
    print(company)
    [print(f"-- {worker}") for worker in companies[company]]
