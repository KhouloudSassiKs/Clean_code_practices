class Musician:
    def __init__(self, name: str, instrument: str, years_active: int):
        self.name = name
        self.instrument = instrument
        self.years_active = years_active
    
    def display(self) -> None:
        """Print musician details including active years."""
        print(f"Name: {self.name}, Instrument: {self.instrument}, Active years: {self.years_active}")

if __name__ == "__main__":
    # Creating an instance with 10 years of activity
    musician = Musician("John", "Guitar", 10)
    musician.display()
