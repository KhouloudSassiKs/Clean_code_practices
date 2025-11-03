class Superhero:
    """A class representing a superhero with an alias and strength level."""

    def __init__(self, alias, strength):
        """Initialize the superhero with an alias and strength."""
        self.__alias = alias
        self.__strength = strength

    def set_alias(self, new_alias):
        """Set a new alias for the superhero."""
        self.__alias = new_alias

    def set_strength(self, new_strength):
        """Set a new strength value for the superhero."""
        self.__strength = new_strength

    def get_alias(self):
        """Return the superhero's alias."""
        return self.__alias

    def get_strength(self):
        """Return the superhero's strength."""
        return self.__strength


if __name__ == "__main__":
    # Create an instance of Superhero
    hero = Superhero("Iron Man", 85)

    # Update alias and strength using setter methods
    hero.set_alias("Doctor Strange")
    hero.set_strength(95)

    # Display the superhero's updated details
    print(f"Superhero: {hero.get_alias()}, Strength: {hero.get_strength()}")
