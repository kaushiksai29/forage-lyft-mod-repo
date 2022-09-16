from car_factory import CarFactory, abstractmethod


class Engine(CarFactory):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass
