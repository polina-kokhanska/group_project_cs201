# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import  bikes
import  station

def main():
    price_for_electro_bike = 5.0
    price_for_regular_bike = 2.0
    station_1 = station.Station([])
    station_2 = station.Station([])
    bike_1 = bikes.RegularBike(38478, station_1)
    bike_2 = bikes.RegularBike(59844, station_1)
    bike_3 = bikes.ElectricBike(39860, station_2)
