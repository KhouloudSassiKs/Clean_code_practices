from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        """Start the engine."""
        pass


class GasEngine(Engine):
    def start(self):
        print("Gas engine starting...")


class Car:
    def __init__(self, engine: Engine):
        """
        Initialize the car with an engine.
        
        Args:
            engine (Engine): Any engine implementing the Engine interface.
        """
        self.engine = engine

    def start(self):
        """Start the car by starting its engine."""
        self.engine.start()


def main():
    gas_engine = GasEngine()
    car = Car(gas_engine)
    car.start()


if __name__ == "__main__":
    main()
