from abc import ABC, abstractmethod

class Authorizer(ABC):
    
    @abstractmethod
    def is_authorized(self) -> bool:
        pass