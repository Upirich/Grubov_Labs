from models.vehicle import *


class Truck(Vehicle):

    def __init__(self, brand, model, year, max_load):
        self.max_load = max_load
        super().__init__(brand, model, year)

    def get_info(self):
        return (self.brand, self.model, self.year, self.max_load)

    def move(self):
        return "Грузовик стоит на месте" if self.speed == 0 else "Грузовик едет"