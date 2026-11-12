from datetime import datetime
from bikes import Bike


class Trip:
    def __init__(self, bike: Bike):
        self.bike = bike
        self.start_time = datetime.now()
        self.end_time = None
        self.trip_time = 0
        self.cost = 0

    def finish(self):
        self.end_time = datetime.now()
        delta = self.end_time - self.start_time
        self.trip_time = delta.total_seconds() / 60
        self.cost = self.bike.price_per_minute * self.trip_time
        return self.cost, self.trip_time


def total_earnings(trips):
    return sum(trip.cost for trip in trips)
        
