from abc import ABC, abstractmethod
from batteries import Battery
from engines import Engine

class Serviceable(ABC):
    def __init__(self) -> None:
        super().__init__()
    @abstractmethod
    def needs_service(self):
        pass

class Car(Serviceable):
    engine = None
    battery = None
    def __init__(self, last_service_date, engine : Engine, battery: Battery):
        self.last_service_date = last_service_date
        self.engine, self.battery = engine, battery

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() | self.battery.needs_service()

