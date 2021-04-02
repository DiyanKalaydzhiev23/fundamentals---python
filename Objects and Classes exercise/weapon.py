class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        text = ""
        if self.bullets > 0:
            self.bullets -= 1
            text = "shooting..."
        else:
            text = "no bullets left"

        return text

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"
