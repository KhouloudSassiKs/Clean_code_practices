from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # Area of equilateral triangle: (sqrt(3)/4) * side^2
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self):
        # Perimeter of equilateral triangle: 3 * side
        return 3 * self.side


if __name__ == "__main__":
    circle = Circle(3)
    print(f"Circle Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")

    rectangle = Rectangle(4, 6)
    print(f"Rectangle Area: {rectangle.area():.2f}, Perimeter: {rectangle.perimeter():.2f}")

    triangle = Triangle(3)
    print(f"Triangle Area: {triangle.area():.2f}, Perimeter: {triangle.perimeter():.2f}")
