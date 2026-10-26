from models.vehicle import *


class Motorcycle(Vehicle):

    def __init__(self, brand, model, year, has_sidecar):
        self.has_sidecar = has_sidecar
        super().__init__(brand, model, year)

    def get_info(self):
        return (self.brand, self.model, self.year, self.has_sidecar)

    def move(self):
        return "Мотоцикл стоит на месте" if self.speed == 0 else "Мотоцикл едет"