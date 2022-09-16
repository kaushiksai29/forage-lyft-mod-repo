from car_factory import CarFactory

from car import Car


class NubbinBattery(Car, CarFactory):
    def __init__(self, last_service_date, current_date, last_service_mileage):
        super().__init__(last_service_mileage)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
