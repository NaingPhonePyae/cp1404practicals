"""Programming language class
Estimated time: 15 min
Actual time: 22 min
"""


class ProgrammingLanguage:
    """Represent a Car object."""

    def __init__(self, name, typing, reflection, year):
        """Create a ProgrammingLanguage"""
        self.typing = typing
        self.name = name
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string in desired format"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if the language is typed dynamically"""
        return self.typing == "Dynamic"
