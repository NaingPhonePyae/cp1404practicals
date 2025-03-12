"""
Guitar class
Estimated time: 20 min
Actual time: 25 min
"""

from prac_06.guitar import Guitar


def main():
    """Run tests to check code"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    gibson = Guitar(name, year, cost)
    another = Guitar("Another Guitar", 2010, 2000)
    print(gibson.name, "get_age() - Expected 103. Got", gibson.get_age())
    print(another.name, "get_age() - Expected 15. Got", another.get_age())
    print(gibson.name, "is_vintage() - Expected True. Got", gibson.is_vintage())
    print(another.name, "is_vintage() - Expected False. Got", another.is_vintage())


if __name__ == "__main__":
    main()
