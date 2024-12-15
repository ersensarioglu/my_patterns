from authorizer import Authorizer

class SMSAuth(Authorizer):
    
    authorized = False
    
    def verify_code(self, code):
        print(f"Verifying SMS code: {code}")
        self.authorized = True
        
    def is_authorized(self) -> bool:
        return self.authorized