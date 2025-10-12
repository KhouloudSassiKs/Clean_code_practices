class Rectangle:
    def __init__(self, width, height):
        """
        Initialize a Rectangle object with given width and height.
        
        Raises:
            ValueError: if width or height are negative.
        
        Features:
        1. Private attributes (__width, __height) for encapsulation.
        2. Error handling to ensure dimensions are positive.
        """
        if width >= 0 and height >= 0:
            # Private attributes: cannot be accessed directly from outside
            self.__width = width
            self.__height = height
        else:
            raise ValueError("Dimensions must be positive")

    @property
    def width(self):
        """
        Property method to provide read-only access to width.
        Allows access like rectangle.width instead of a traditional getter.
        """
        return self.__width

    @property
    def height(self):
        """
        Property method to provide read-only access to height.
        Allows access like rectangle.height instead of a traditional getter.
        """
        return self.__height

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle.
        Formula: 2 * (width + height)
        """
        return 2 * (self.__width + self.__height)

    def area(self):
        """
        Compute and return the area of the rectangle.
        Formula: width * height
        """
        return self.__width * self.__height


def main():
    # Example usage of Rectangle class
    rectangle = Rectangle(5.0, 3.0)
    print("Width:", rectangle.width)
    print("Height:", rectangle.height)
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())


if __name__ == "__main__":
    main()
