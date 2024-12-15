from payments import PaymentProcessor
from authorizer import Authorizer

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True
                
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Cannot process order: SMS verification is not complete")
        print("Processing PayPal payment")
        print(f"Verifying security code: {self.email_address}")
        order.status = "paid"