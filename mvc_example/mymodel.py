from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def generate_uuid(self):
        pass
    
    @abstractmethod
    def clear_uuid(self):
        pass
    
    @abstractmethod
    def get_uuid(self):
        pass

class TkModel(Model):
    def __init__(self):
        self.uuid = ""
    
    def generate_uuid(self, Uuid):
        self.uuid = Uuid.generate()
               
    def clear_uuid(self):
        self.uuid = "" 
        
    def get_uuid(self):
        return self.uuid
    
 