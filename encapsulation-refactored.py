"""
This script models a simple library system using OOP principles.

Update note:
Removed direct access to `Book` and `User` attributes from the `Library` class.
Instead, interaction now happens through getter and behavior methods,
inline with encapsulation principles.
"""

class Library:
    def check_out_book(self, user, book):
        """Delegate the checkout action to the User class."""
        user.borrow_book(book)


class User:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def borrow_book(self, book):
        """Handle the logic for borrowing a book."""
        print(f"{self._name} borrowed {book.get_title()}")


class Book:
    def __init__(self, title):
        self._title = title
    
    def get_title(self):
        return self._title


def main():
    user = User("John Doe")
    book = Book("Python Programming")
    library = Library()
    library.check_out_book(user, book)


if __name__ == "__main__":
    main()
