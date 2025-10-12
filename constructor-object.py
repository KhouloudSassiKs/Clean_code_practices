class Book:
    def __init__(self, title, author, publisher, year, genre, price):
        """
        Initialize a Book instance.

        Note:
        - 'author' should be an instance of Author class.
        - 'publisher' should be an instance of Publisher class.
        - Consider grouping author and publisher details into separate classes
          (done here) to simplify constructor and improve code readability.
        """
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.price = price
    
    def __str__(self):
        """
        Return a human-readable string representation of the book.
        Accesses attributes of author and publisher objects.
        """
        return (f"Book[Title={self.title}, Author={self.author.author_name}, "
                f"Publisher={self.publisher.publisher_name}, Year={self.year}, "
                f"Genre={self.genre}, Price={self.price}]")

class Author:
    def __init__(self, author_name, author_email):
        """
        Initialize an Author instance.
        """
        self.author_name = author_name
        self.author_email = author_email
    
class Publisher:
    def __init__(self, publisher_name, publisher_address):
        """
        Initialize a Publisher instance.
        """
        self.publisher_name = publisher_name
        self.publisher_address = publisher_address
        

def main():
    """
    Example usage of Book, Author, and Publisher classes.
    
    Notes:
    - You can consider using a builder pattern or refactor the Book constructor
      if the number of attributes grows larger or for better scalability.
    """
    author = Author("J.K. Rowling", "jk.rowling@example.com")
    publisher = Publisher("Bloomsbury Publishing", "50 Bedford Square, London")
    
    book = Book(
        "Harry Potter and the Philosopher's Stone",
        author,
        publisher,
        1997,
        "Fantasy",
        39.99
    )
    print(book)


if __name__ == "__main__":
    main()
