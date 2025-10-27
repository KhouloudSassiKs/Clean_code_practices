from abc import ABC, abstractmethod

# Abstract base class defining a common interface for all product calculators
class ProductCalculator(ABC):
    @abstractmethod
    def calculate_price(self, base_price):
        """Calculate the final price for a product."""
        pass


# Concrete class for Book — no additional pricing rules
class Book(ProductCalculator):
    def calculate_price(self, base_price):
        return base_price


# Concrete class for Food — includes a tax calculation
class Food(ProductCalculator):
    def calculate_price(self, base_price):
        return base_price + base_price * 0.07


def main_program():
    # Create product instances
    book = Book()
    food_item = Food()

    # Calculate prices using polymorphism
    book_price = book.calculate_price(29.99)
    food_price = food_item.calculate_price(0.99)

    print(f"Price of Book: ${book_price:.2f}")
    print(f"Price of Food: ${food_price:.2f}")


if __name__ == "__main__":
    main_program()
