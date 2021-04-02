header = input()
article = input()
print(f"<h1>\n    {header}\n</h1>")
print(f"<article>\n    {article}\n</article>")

data = input()

while data != "end of comments":
    print(f"<div>\n    {data}\n</div>")
    data = input()
