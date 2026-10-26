from models.vehicle import *


class Bus(Vehicle):

    def __init__(self, brand, model, year, number_of_way, people):
        self.num = number_of_way
        self.people = people
        super().__init__(brand, model, year)

    def get_info(self):
        return (self.brand, self.model, self.year, self.num, self.people)

    def move(self):
        return "Автобус стоит на месте" if self.speed == 0 else "Автобус движется"

    def __str__(self):
        return f"Автобус номер {self.num}, бренда {self.brand}, модели {self.model} и {self.year} года. Внутри автобуса {self.people} человек."