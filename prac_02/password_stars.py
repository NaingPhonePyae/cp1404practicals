"""password stars"""
MINIMUM_LENGTH = 3


def main():
    password = get_password()
    for i in range(len(password)):
        print("*", end="")


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid")
        password = input("Password: ")
    return password


main()
