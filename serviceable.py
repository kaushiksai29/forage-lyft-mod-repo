from sys import implementation
from car import Car, abstractmethod

class Serviceable(Car):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass
