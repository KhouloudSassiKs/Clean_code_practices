class Library:
    def __init__(self):
        """
        Initialize the Library with a private list of books.
        __books is private to prevent direct modification from outside.
        """
        self.__books = []

    @property
    def books(self):
        """
        Property to provide read-only access to the list of books.
        Returns a copy of the internal list to prevent external modification.
        """
        return self.__books.copy()  # return a copy, not the original list

    def add_book(self, book):
        """
        Add a book to the library if it does not already exist.
        Raises ValueError if the book is already in the library.
        """
        if book not in self.__books:
            self.__books.append(book)
        else:
            raise ValueError("This book is already in your list")

    def remove_book(self, book):
        """
        Remove a book from the library if it exists.
        Raises ValueError if the book does not exist.
        """
        if book in self.__books:
            self.__books.remove(book)
        else:
            raise ValueError("This book does not exist in the book list")


def main():
    # Example usage
    library = Library()
    library.add_book("Clean Code")
    library.add_book("Design Patterns")
    library.add_book("Refactoring")
    library.remove_book("Design Patterns")

    print("Library Books:")
    for book_title in library.books:
        print(book_title)


if __name__ == "__main__":
    main()
