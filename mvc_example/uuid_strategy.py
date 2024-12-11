from abc import ABC, abstractmethod 

class UuidStrategy(ABC): 
    @abstractmethod 
    def generate(self) -> str:
        pass