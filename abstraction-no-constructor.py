from abc import ABC, abstractmethod


# Abstract class Appliance
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# Television class inherits from Appliance
class Television(Appliance):
    def turn_on(self):
        print("The television is now ON.")

    def turn_off(self):
        print("The television is now OFF.")


# WashingMachine class inherits from Appliance
class WashingMachine(Appliance):
    def turn_on(self):
        print("The washing machine is now ON.")

    def turn_off(self):
        print("The washing machine is now OFF.")


if __name__ == "__main__":
    # Create an instance of Television and call its methods
    tv = Television()
    tv.turn_on()
    tv.turn_off()

    # Create an instance of WashingMachine and call its methods
    wm = WashingMachine()
    wm.turn_on()
    wm.turn_off()
