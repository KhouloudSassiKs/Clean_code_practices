from abc import ABC, abstractmethod
from typing import List


# --- Abstract Animal Class ---
class Animal(ABC):
    @abstractmethod
    def feed(self) -> None:
        """Feed the animal."""
        pass


# --- Playable Interface ---
class Playable(ABC):
    @abstractmethod
    def play(self) -> None:
        """Play with the animal."""
        pass


# --- Concrete Animals ---
class Dog(Animal, Playable):
    def feed(self) -> None:
        print("Feeding the dog with dog food.")

    def play(self) -> None:
        print("Playing fetch with the dog.")


class Cat(Animal, Playable):
    def feed(self) -> None:
        print("Feeding the cat with cat food.")

    def play(self) -> None:
        print("Playing with the cat using a ball of yarn.")


class Bird(Animal):
    def feed(self) -> None:
        print("Feeding the bird with seeds.")


# --- Helper Functions ---
def feed_animal(animal: Animal) -> None:
    """Feed any animal."""
    animal.feed()


def play_with_animal(animal: Playable) -> None:
    """Play with any playable animal."""
    animal.play()


# --- Main Program ---
if __name__ == "__main__":
    animals: List[Animal] = [Dog(), Cat(), Bird()]

    for animal in animals:
        feed_animal(animal)
        # Only play with animals that implement Playable
        if isinstance(animal, Playable):
            play_with_animal(animal)
