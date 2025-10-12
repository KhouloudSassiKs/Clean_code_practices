class Weapon:
    """
    Represents a weapon with a specific attack behavior.
    Demonstrates encapsulation of weapon functionality.
    """

    def __init__(self, weapon_name):
        # Store weapon type
        self.weapon = weapon_name

    def attack(self):
        """
        Perform an attack based on the weapon type.
        """
        if self.weapon == "Sword":
            print("Swinging the sword!")
        elif self.weapon == "Bow":
            print("Shooting an arrow!")
        else:
            print("Unknown weapon!")


class Hero:
    """
    Represents a generic hero who uses a weapon.
    Demonstrates composition — a Hero 'has-a' Weapon.
    """

    def __init__(self, weapon):
        self.weapon = weapon


class Archer(Hero):
    """
    Represents an Archer, a specialized Hero.
    Inherits from Hero to reuse weapon handling.
    """

    def __init__(self, weapon):
        # Call the base class constructor
        super().__init__(weapon)


def main():
    """
    Demonstrates composition and inheritance:
    - A Hero and Archer both 'have' a Weapon.
    - Attack behavior depends on the Weapon class.
    """
    sword = Weapon("Sword")
    bow = Weapon("Bow")

    hero = Hero(sword)
    hero.weapon.attack()  # Swinging the sword!

    archer = Archer(bow)
    archer.weapon.attack()  # Shooting an arrow!


if __name__ == "__main__":
    main()
