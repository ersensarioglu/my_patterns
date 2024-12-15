from authorizer import Authorizer

class NotARobot(Authorizer):
    authorized = False
    
    def not_a_robot(self):
        print("I'm not a robot!")
        self.authorized = True