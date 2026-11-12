class Bike:
    def __init__(self, id: int, price_per_minute: float):
        self.id = id
        self.price_per_minute = price_per_minute


class RegularBike(Bike):
    def __init__(self, id: int):
        super().__init__(id, 2.0)


class ElectricBike(Bike):
    def __init__(self, id: int):
        super().__init__(id, 5.0)