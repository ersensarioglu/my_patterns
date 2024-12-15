from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    
    @abstractmethod
    def pay(self, order):
        pass
    
# We can also define an abstract method for SMS verification
class PaymentProcessor_SMS(PaymentProcessor):
        
    @abstractmethod
    def auth_sms(self,code):
        pass
    