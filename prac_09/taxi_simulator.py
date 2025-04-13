from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(current_taxi, taxis)
        elif choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(current_taxi, taxis):
    """Choose taxi from the list."""
    print("Taxis available: ")
    display_taxis(taxis)
    try:
        taxi_chosen = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_chosen]
    except IndexError:
        print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return current_taxi


def display_taxis(taxis):
    """Display list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(current_taxi, total_bill):
    """Drive the taxi using input current taxi and calculate the fare"""
    if current_taxi:
        current_taxi.start_fare()
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        taxi_fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${taxi_fare:.2f}")
        total_bill += taxi_fare
    else:
        print("You need to choose a taxi before you can drive")
    return total_bill


if __name__ == '__main__':
    main()
