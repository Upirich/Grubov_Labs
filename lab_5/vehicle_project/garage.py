class Garage:

    def __init__(self):
        self.sp = []

    def add_vehicle(self, veh):
        self.sp.append(veh)

    def remove_vehicle(self, veh):
        self.sp.remove(veh)

    def show_all(self):
        print(*self.sp)

    def find_by_brand(self, brand):
        for veh in self.sp:
            if veh.brand == brand:
                return veh
        return None
    