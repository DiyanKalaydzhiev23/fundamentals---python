class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        response = ""

        if money >= self.price and self.owner is None:
            change = money - self.price
            response = f"Successfully bought a {self.type}. Change: {change:.2f}"
            self.owner = owner
        else:
            if money < self.price:
                response = "Sorry, not enough money"
            if self.owner is not None:
                response = "Car already sold"

        return response

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        result = ""
        if self.owner is not None:
            result = f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            result = f"{self.model} {self.type} is on sale: {self.price}"

        return result


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)

