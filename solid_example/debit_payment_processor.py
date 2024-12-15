from payments import PaymentProcessor_SMS

class DebitPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False
        
    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True
        
    def pay(self, order):
        if not self.verified:
            raise Exception("Cannot process order: SMS verification is not complete")
        print("Processing debit payment")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"