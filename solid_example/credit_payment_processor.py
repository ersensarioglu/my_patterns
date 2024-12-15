from payments import PaymentProcessor

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code  
      
    def pay(self, order):
        print("Processing credit payment")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"