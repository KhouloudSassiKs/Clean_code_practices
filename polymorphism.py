from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def feed(self):
        """Feed the animal. Must be implemented by subclasses."""
        pass


class Dog(Animal):
    def feed(self):
        print("Feeding the dog with dog food.")


class Cat(Animal):
    def feed(self):
        print("Feeding the cat with cat food.")


class Bird(Animal):
    def feed(self):
        print("Feeding the bird with bird seeds.")


def feed_animal(animal: Animal):
    """Feed any animal using polymorphism."""
    animal.feed()


if __name__ == "__main__":
    animals = [Dog(), Cat(), Bird()]
    for animal in animals:
        feed_animal(animal)
