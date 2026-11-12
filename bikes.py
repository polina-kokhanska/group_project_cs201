from enum import Enum


class BikeStatus(Enum):
    AVAILABLE = 0
    TAKEN = 1


class Bike:
    def __init__(self, id: int, parent_station, price_per_minute: float):
        self.id = id
        self.parent_station = parent_station
        self.price_per_minute = price_per_minute
        self.status = BikeStatus.AVAILABLE


class RegularBike(Bike):
    def __init__(self, id: int, parent_station):
        super().__init__(id, parent_station, 2.0)


class ElectricBike(Bike):
    def __init__(self, parent_station, id: int):
        super().__init__(id, parent_station, 5.0)