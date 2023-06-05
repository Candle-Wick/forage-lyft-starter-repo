
from engines import *
from batteries import *
from car import Car

def CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_milage):   
        engine = CapuletEngine(current_mileage, last_service_milage)
        battery = SpindlerBattery(last_service_date)
        new_car = Car(last_service_date=last_service_date, engine=engine, battery=battery)
        return new_car
    def create_glissade(current_date, last_service_date, current_mileage, last_service_milage):
        engine = WilloughbyEngine(current_mileage, last_service_milage)
        battery = SpindlerBattery(last_service_date)
        new_car = Car(last_service_date=last_service_date, engine=engine, battery=battery)
        return new_car
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_milage):
        engine = SternmanEngine(False)
        battery = SpindlerBattery(last_service_date)
        new_car = Car(last_service_date=last_service_date, engine=engine, battery=battery)
        return new_car
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_milage):
        engine = WilloughbyEngine(current_mileage, last_service_milage)
        battery = NubbinBattery(last_service_date)
        new_car = Car(last_service_date=last_service_date, engine=engine, battery=battery)
        return new_car
    def create_thovex(current_date, last_service_date, current_mileage, last_service_milage):
        engine = CapuletEngine(current_mileage, last_service_milage)
        battery = NubbinBattery(last_service_date)
        new_car = Car(last_service_date=last_service_date, engine=engine, battery=battery)
        return new_car

