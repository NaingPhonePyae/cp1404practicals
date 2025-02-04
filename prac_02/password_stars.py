"""password stars"""
MINIMUM_LENGTH = 3


def main():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid")
        password = input("Password: ")
    for i in range(len(password)):
        print("*", end="")


main()
