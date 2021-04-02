languages = {}
banned = []
results = {}

data = input().split("-")

while "exam finished" not in data:
    if "banned" in data:
        banned.append(data[0])
        data = input().split("-")
        continue

    name = data[0]
    language = data[1]
    points = int(data[2])
    current_points = 0

    if language in languages:
        languages[language] += 1
        if name in results:
            if points > results[name]:
                results[name] = points
        else:
            results[name] = points
    else:
        languages[language] = 1
        results[name] = points

    data = input().split("-")

results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
languages = dict(sorted(languages.items(), key=lambda x: (-x[1], x[0])))

print("Results:")

for name in results:
    if name in banned:
        continue
    else:
        print(f"{name} | {results[name]}")

print("Submissions:")

[print(f"{language} - {languages[language]}") for language in languages]
