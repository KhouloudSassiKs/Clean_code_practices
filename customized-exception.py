# --- Custom Exceptions ---
class CustomException(Exception):
    """Base class for all library-related exceptions."""

    def __init__(self, message: str, book_id=None, user_id=None):
        super().__init__(message)
        self.message = message
        self.book_id = book_id
        self.user_id = user_id


class BookNotAvailableException(CustomException):
    """Raised when a requested book is not available."""
    pass


class BookNotFoundException(CustomException):
    """Raised when a requested book cannot be found."""
    pass


class InvalidUserException(CustomException):
    """Raised when a user is not valid."""
    pass


# --- Repository simulating book operations ---
class BookRepository:
    """Simulates a repository that manages book data."""

    def is_book_available(self, book_id: str) -> bool:
        """Check if a book is available for borrowing."""
        if book_id == "00000":
            raise BookNotFoundException("Book not found", book_id=book_id)
        return True

    def is_valid_user(self, user_id: str) -> bool:
        """Check if the given user is valid."""
        if user_id != "user1":
            raise InvalidUserException("Invalid user", user_id=user_id)
        return True

    def update_book_status(self, book_id: str, is_available: bool) -> None:
        """Update a book’s availability status."""
        if book_id == "error":
            raise BookNotAvailableException("Failed to update book status", book_id=book_id)
        status = "Available" if is_available else "Not available"
        print(f"Book status updated: {status}")


# --- Service handling library logic ---
class LibraryService:
    """Handles core library operations such as borrowing books."""

    def __init__(self):
        self.book_repository = BookRepository()

    def borrow_book(self, book_id: str, user_id: str) -> None:
        """Attempt to borrow a book for a user."""
        try:
            if not self.book_repository.is_book_available(book_id):
                raise BookNotAvailableException("Book is not available", book_id=book_id)
            if not self.book_repository.is_valid_user(user_id):
                raise InvalidUserException("User is not valid", user_id=user_id)

            self.book_repository.update_book_status(book_id, False)
            print("Book borrowed successfully!")

        except CustomException as e:
            print(f"Borrowing failed: {e.message}")
            if e.book_id:
                print(f"  Book ID: {e.book_id}")
            if e.user_id:
                print(f"  User ID: {e.user_id}")


# --- Main Program ---
def main():
    library_service = LibraryService()

    print("=== Test Case 1: Successful Borrow ===")
    library_service.borrow_book("12345", "user1")

    print("\n=== Test Case 2: Invalid User ===")
    library_service.borrow_book("12345", "user2")

    print("\n=== Test Case 3: Book Not Found ===")
    library_service.borrow_book("00000", "user1")

    print("\n=== Test Case 4: Book Update Error ===")
    library_service.borrow_book("error", "user1")


if __name__ == "__main__":
    main()
