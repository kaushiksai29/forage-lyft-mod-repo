from car import Car
from datetime import datetime

from engine.model import thovex

class CarFactory():
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        calliope = CarFactory()
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        return Car(calliope)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        glissade = CarFactory()
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        return Car(glissade)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        palindrome = CarFactory()
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.warning_light_on = False

        return Car(palindrome)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        rorschach = CarFactory()
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        return Car(rorschach)



    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        thovex = CarFactory()
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
        return Car(thovex)