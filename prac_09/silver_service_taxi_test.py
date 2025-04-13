from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Run test for SilverServiceTaxi class."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

    assert taxi.fuel == 82, f"Expected fuel to be 82, but got {taxi.fuel}"
    assert taxi.get_fare() == 48.78, f"Expected fare to be 72.4, but got {taxi.get_fare()}"


if __name__ == '__main__':
    main()
