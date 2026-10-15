class Vehicle:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0

    def accelerate(self, value):
        self.speed += value

    def brake(self, value):
        if self.speed - value < 0:
            self.speed = 0
        else:
            self.speed -= value

    def stop(self):
        self.speed = 0

    def get_info(self):
        print(self.speed)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError('Скорость не может быть отрицательной')
        self._speed = value

    def __str__(self):
        return(f'Транспорт: {self.brand}, модели: {self.model}, {self.year} года производства. Скорость в данный момент: {self.speed}')
    
    
    