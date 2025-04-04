"""
wimbledon
Estimate: 20 minutes
Actual: 27 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """program to read file and print details about Wimbledon champions and countries"""
    records = load_details(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


def process_records(records):
    """create dictionary of champions to set of countries from details"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, countries


def load_details(filename):
    """Load details from file in list"""
    details = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            details.append(parts)
    return details


main()
