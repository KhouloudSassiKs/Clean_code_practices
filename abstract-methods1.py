from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass

    @abstractmethod
    def description(self):
        """Provide a text description of the shape."""
        pass


class Circle(Shape):
    """Represents a circle shape."""

    def __init__(self, radius):
        """Initialize a circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * 3.14159 * self.radius

    def description(self):
        """Provide a description of the circle."""
        print("This is a circle.")


class Rectangle(Shape):
    """Represents a rectangle shape."""

    def __init__(self, width, height):
        """Initialize a rectangle with a given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def description(self):
        """Provide a description of the rectangle."""
        print("This is a rectangle.")


if __name__ == "__main__":
    """Demonstrate the use of abstract classes with concrete shape implementations."""

    shape = Circle(3)
    print(f"Shape Area: {shape.area()}, Perimeter: {shape.perimeter()}")
    shape.description()

    print()  # For clean output separation

    shape = Rectangle(4, 6)
    print(f"Shape Area: {shape.area()}, Perimeter: {shape.perimeter()}")
    shape.description()
