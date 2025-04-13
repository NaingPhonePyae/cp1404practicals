class Band:
    """Represent a Band class."""

    def __init__(self, name=""):
        """Initialise a band instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        instrument_string = ",".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({instrument_string})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their first (or no) instrument."""
        for musician in self.musicians:
            return musician.play()
