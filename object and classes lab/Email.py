class Email:
    def __init__(self, sender, receiver, content, is_send=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = is_send

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


mail = input().split(" ")
emails = []

while "Stop" not in mail:
    email = Email(mail[0], mail[1], mail[2])
    emails.append(email)
    mail = input().split(" ")

indexes = list(map(lambda c: int(c), input().split(", ")))

for x in indexes:
    emails[x].send()

for email in emails:
    print(email.get_info())
