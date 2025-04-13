from prac_09.unreliable_car import UnreliableCar


def main():
    """Run tests for UnreliableCar class"""
    reliable_car = UnreliableCar("Good", 100, 90)
    unreliable_car = UnreliableCar("Junk", 100, 10)

    for distance in range(1, 26):
        print(f"drive {distance:2} km: {reliable_car.name} drove {reliable_car.drive(distance)}km")
        print(f"drive {distance:2} km: {unreliable_car.name} drove {unreliable_car.drive(distance)}km")

    print(reliable_car)
    print(unreliable_car)


if __name__ == '__main__':
    main()
