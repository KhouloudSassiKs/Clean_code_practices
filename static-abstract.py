from abc import ABC, abstractmethod


# --- Abstract Fruit Class ---
class Fruit(ABC):
    @abstractmethod
    def get_description(self) -> str:
        """Return a description of the fruit."""
        pass


# --- Concrete Fruits ---
class Apple(Fruit):
    def get_description(self) -> str:
        return "This is an apple."


class Banana(Fruit):
    def get_description(self) -> str:
        return "This is a banana."


# --- Fruit Factory ---
class FruitFactory:
    """Factory class responsible for creating fruit objects."""

    @staticmethod
    def order_fruit(fruit_name: str) -> Fruit:
        """Create and return a fruit object based on the name."""
        if fruit_name.lower() == "apple":
            return Apple()
        elif fruit_name.lower() == "banana":
            return Banana()
        else:
            raise ValueError(f"Unknown fruit type: {fruit_name}")


# --- Fruit Store ---
class FruitStore:
    """Store class that uses a FruitFactory to order fruits."""

    def __init__(self, fruit_factory: FruitFactory):
        self.factory = fruit_factory

    def order_fruit(self, fruit_name: str) -> Fruit:
        """Order a fruit using the factory."""
        return self.factory.order_fruit(fruit_name)


# --- Main Program ---
def main():
    factory = FruitFactory()
    store = FruitStore(factory)

    apple = store.order_fruit("Apple")
    print(apple.get_description())

    banana = store.order_fruit("Banana")
    print(banana.get_description())


if __name__ == "__main__":
    main()
