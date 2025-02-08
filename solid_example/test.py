from abc import ABC, abstractmethod

# Abstraction (interface)
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

@abstractmethod
def turn_off(self):
    pass

# Low-level module: LightBulb
class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb is turned ON.")

    def turn_off(self):
        print("LightBulb is turned OFF.")

# Low-level module: LEDLight
class LEDLight(Switchable):
    def turn_on(self):
        print("LED Light is turned ON.")

    def turn_off(self):
        print("LED Light is turned OFF.")

# High-level module: LightSwitch depends on abstraction (Switchable)
class LightSwitch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self, command):
        if command == "on":
            self.device.turn_on()
        elif command == "off":
            self.device.turn_off()

# Usage
bulb = LightBulb()
switch = LightSwitch(bulb)
switch.operate("on")   # Output: LightBulb is turned ON.
switch.operate("off")  # Output: LightBulb is turned OFF.

led = LEDLight()
switch_led = LightSwitch(led)
switch_led.operate("on")  # Output: LED Light is turned ON.
switch_led.operate("off") # Output: LED Light is turned OFF.
