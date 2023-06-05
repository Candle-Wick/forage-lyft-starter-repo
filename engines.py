from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def needs_service():
        pass

class CapuletEngine(ABC):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
    
class WilloughbyEngine(ABC):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
    
class SternmanEngine(ABC):
    def __init__(self, warning_light_is_on):
        super().__init__()
        self.warning_light_is_on = warning_light_is_on
        
    def needs_service(self):
        return self.cwarning_light_is_onheck_engine_light