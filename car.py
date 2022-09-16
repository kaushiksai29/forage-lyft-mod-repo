from car_factory import CarFactory, abstractmethod
from engine import Engine
from battery import Battery

class Car(CarFactory):
    def __init__(self, Engine, Battery):
        super().__init__(Engine, Battery)
        self.engine = Engine
        self.battery = Battery

    @abstractmethod
    def needs_service(self):
        pass
