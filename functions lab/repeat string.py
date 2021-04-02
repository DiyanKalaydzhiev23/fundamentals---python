word = input()
times = int(input())


def repeat():
    text = ""
    for _ in range(times):
        text += word
    print(text)


repeat()
