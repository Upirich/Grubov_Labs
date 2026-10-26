from models.vehicle import *


class Car(Vehicle):

    def __init__(self, brand, model, year, doors):
        self.doors = doors
        super().__init__(brand, model, year)

    def get_info(self):
        return (self.brand, self.model, self.year, self.doors)

    def move(self):
        return "Машина стоит на месте" if self.speed == 0 else "Машина едет"