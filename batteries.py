from abc import ABC, abstractmethod
from datetime import datetime

class Battery(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def needs_service():
        pass

class SpindlerBattery(Battery):
    last_service_date = None

    def __init__(self, last_service_date) -> None:
        super().__init__()
        last_service_date=last_service_date

    def needs_service():
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date()
    
class NubbinBattery(Battery):
    last_service_date = None

    def __init__(self, last_service_date) -> None:
        super().__init__()
        last_service_date=last_service_date

    def needs_service():
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date()


