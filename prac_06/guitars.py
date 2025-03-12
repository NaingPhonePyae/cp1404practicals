"""
Store guitar details program
Estimated time: 30 min
Actual time: 35 min
"""

from prac_06.guitar import Guitar


def play_guitar():
    """Store guitar details program"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")

    # guitars.append(Guitar("Frender strocaster", 2014, 765.40))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        name_format = max(len(guitar.name) for guitar in guitars)
        cost_format = max(len(str(guitar.cost)) for guitar in guitars) + 3
        for i, guitar in enumerate(guitars, 1):
            print(
                f"Guitar {i}:  {guitar.name:>{name_format}} ({guitar.year}), worth $ {guitar.cost:>{cost_format},.2f} "
                f"{"(vintage)" if guitar.is_vintage() else ""}")
    else:
        print("Where are the guitars?")


play_guitar()
