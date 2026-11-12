class Bike:
    def __init__(self, id: int, price_per_hour: float):
        self.id = id
        self.price_per_hour = price_per_hour


class RegularBike(Bike):
    def __init__(self, id: int):
        self.price_per_hour = 2.0
        super().__init__(id, self.price_per_hour)


class ElectricBike(Bike):
    def __init__(self, id: int):
        self.price_per_hour = 5.0
        super().__init__(id, self.price_per_hour)