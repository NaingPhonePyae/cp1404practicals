"""Program for storing guitar details"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file, store in list, add new guitars in list, store them to file"""
    guitars = []
    read_files(guitars)

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    add_guitar(guitars)
    guitars.sort()

    store_guitars(guitars)


def read_files(guitars):
    """Read details from file and add to list"""
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar_to_add = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar_to_add)


def store_guitars(guitars):
    """Store guitar details in file"""
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{float(guitar.cost):.2f}\n")


def add_guitar(guitars):
    """Add new input guitar details in list"""
    print("My new guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")


if __name__ == "__main__":
    main()
