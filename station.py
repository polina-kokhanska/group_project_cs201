from bikes import Bike, BikeStatus


class Station:
    def __init__(self, available_bikes: list[Bike]):
        self.available_bikes = available_bikes

    def is_bike_available(self, bike: Bike):
        return bike in self.available_bikes and bike.status == BikeStatus.AVAILABLE