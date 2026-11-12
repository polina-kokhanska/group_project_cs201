import datetime

from bikes import Bike


class Client:
    def __init__(self,name,balance,ride_time):
        self.name=name
        self.balance=balance
        self.ride_time=0
        self.bike=None

    def take_bike(self,bike_id,station):
        time = datetime.now()
        if self.bike is None:
            return None
        for bike in station.bikes:
            if bike.bike_id == bike_id and bike.status==BikeStatus.AVAILABLE:
                bike.status=BikeStatus.TAKEN
                bike.parent_station=None
                station.bikes.remove(bike)
                self.bike=bike
                return bike,time.time()
    def return_bike(self,bike_id, station):
        bike = self.bike
        if bike is None or bike.id != bike_id or bike.status != BikeStatus.TAKEN:
            return None

        bike.status = BikeStatus.AVAILABLE
        bike.parent_station = station
        station.bikes.append(bike)
        self.bike = None
        time = datetime.now()
        return bike,time.time()



    def charge(self,ride_time,bike):
        cost=ride_time*bike.price_per_hour
        if self.balance<cost:
            return None
        else:
            return self.balance-cost
