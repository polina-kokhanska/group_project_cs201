from bikes import Bike


class Trip:
    def __init__(self, start_time, end_time,):
        start_time = datetime.now()
        self.end_time = None

    def finish(self, end_time,bike:Bike,start_time,):
        self.end_time = datetime.now()
        trip_time = self.end_time - self.start_time
        self.bike.price_per_minute = bike.price_per_minute
        cost = bike.price_per_minute * trip_time
        return cost, trip_time
    def total_earnings(self,bike:Bike,cost, number_of_clients):
        total_earnings = cost*number_of_clients
        return total_earnings
        
