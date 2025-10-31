class Movie:
    """A class to represent a movie with title, genre, and release year."""

    def __init__(self, title, genre, release_year):
        self.title = title
        self.genre = genre
        self.release_year = release_year

    def display(self):
        """Display the movie details."""
        print(f"Title: {self.title}, Genre: {self.genre}, Release Year: {self.release_year}")

    def update_title(self, new_title):
        """Update the movie's title."""
        self.title = new_title


if __name__ == "__main__":
    # Create a movie object
    movie = Movie("Inception", "Sci-Fi", 2010)
    movie.display()

    # Update the movie title
    movie.update_title("Interstellar")

    # Display updated details
    movie.display()
