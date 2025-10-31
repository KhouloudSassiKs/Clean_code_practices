class Film:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def display(self):
        print(f"Title: {self.title}, Director: {self.director}")


if __name__ == "__main__":
    # TODO: Create a new film object named 'inception' with title "Inception" and director "Christopher Nolan"
    inception = Film("Inception", "Christopher Nolan")

    # TODO: Print the film attributes to the console
    inception.display()
