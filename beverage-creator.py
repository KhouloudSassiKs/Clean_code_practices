from abc import ABC, abstractmethod

# Abstract Product
class Beverage(ABC):
    @abstractmethod
    def drink(self):
        pass


# Concrete Products
class Coffee(Beverage):
    def drink(self):
        print("Drinking Coffee")


class Tea(Beverage):
    def drink(self):
        print("Drinking Tea")


class Juice(Beverage):
    def drink(self):
        print("Drinking Juice")


# Abstract Creator
class BeverageCreator(ABC):
    @abstractmethod
    def create_beverage(self):
        pass


# Concrete Creators
class CoffeeCreator(BeverageCreator):
    def create_beverage(self):
        return Coffee()


class TeaCreator(BeverageCreator):
    def create_beverage(self):
        return Tea()


class JuiceCreator(BeverageCreator):
    def create_beverage(self):
        return Juice()


# Client Code
if __name__ == "__main__":
    coffee = CoffeeCreator().create_beverage()
    tea = TeaCreator().create_beverage()
    juice = JuiceCreator().create_beverage()

    coffee.drink()
    tea.drink()
    juice.drink()
