from prac_09.taxi import Taxi


def run_tests():
    """Run tests for taxi class"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, Current fare: ${my_taxi.get_fare()}")


if __name__ == '__main__':
    run_tests()
