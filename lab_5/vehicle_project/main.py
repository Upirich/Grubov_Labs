from models.car import *
from models.motorcycle import *
from models.truck import *
from garage import *
from models.bus import *


def main():
    # v1 = Vehicle('ferrari', 'supercar', 1970)
    # v2 = Vehicle('bmw', 'x8', 2000)

    # print(v1.brand, v1.model, v1.year)
    # print(v2.brand, v2.model, v2.year)

    # v1.accelerate(10)
    # v1.get_info()
    # v1.brake(6)
    # v1.get_info()
    # v1.brake(10)
    # v1.get_info()
    # v1.accelerate(20)
    # v1.stop()
    # v1.get_info()

    # print(v1)

    # car1 = Car('lada', 'priora', 2000, 5)
    # print(car1.get_info())

    # car2 = Car('lada', 'vesta', 2010, 5)
    # truck2 = Truck('MAN', 'BIG', 2015, 2)
    # motorcycle2 = Motorcycle('Kawasaki', 'gut', 2000, 2)
    # sp = [car2, truck2, motorcycle2]
    # for veh in sp:
    #     print(veh.move())
    #     print(veh.get_info())

    car3 = Car('lada', 'vesta', 2010, 5)
    truck3 = Truck('MAN', 'BIG', 2015, 2)
    motorcycle3 = Motorcycle('Kawasaki', 'gut', 2000, 2)
    bus3 = Bus('Лиаз', '2503', 1999, 90, 20)
    gar = Garage()
    gar.add_vehicle(car3)
    gar.add_vehicle(truck3)
    gar.add_vehicle(motorcycle3)
    gar.add_vehicle(bus3)
    gar.show_all()
    print(gar.find_by_brand('lada'))


if __name__ == '__main__':
    main()