from sys import implementation
from car import Car, abstractmethod
from car_factory import CarFactory, abstractmethod

class Serviceable(CarFactory):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass
