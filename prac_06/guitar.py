"""
Guitar class
Estimated time: 20 min
Actual time: 25 min
"""

THIS_YEAR = 2025


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Create a Guitar details"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string in desired format"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar"""
        age = THIS_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if the guitar is vintage"""
        return self.get_age() >= 50
