from abc import ABC, abstractmethod
from datetime import datetime

class Tyre(ABC):
    tires = []
    def __init__(self, tires) -> None:
        super().__init__()
        self.tires = tires
    
    @abstractmethod
    def needs_service():
        pass

class CarriganTyre(Tyre):
    def __init__(self, tires) -> None:
        super().__init__(tires)

    def needs_service():
        for i in self.tires:
            if i <= 0.9:
                return True
        return False

class OctoprimeTyre(Tyre):
    def __init__(self, tires) -> None:
        super().__init__(tires)

    def needs_service():
        return sum(self.tires) >= 3
