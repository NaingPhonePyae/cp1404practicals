"""Program for storing guitar details"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file, store in list"""
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar_to_add = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar_to_add)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
