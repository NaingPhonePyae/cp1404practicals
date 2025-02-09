MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

MENU = ("(G)et a valid score\n"
        "(P)rint result\n"
        "(S)how stars\n"
        "(Q)uit")


def main():
    score = int(input("Score: "))
    while score not in range(0, 101):
        print("Invalid score")
        score = int(input("Score: "))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Score: "))
            while score not in range(0, 101):
                print("Invalid score")
                score = int(input("Score: "))
        elif choice == "P":
            if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
                result = "Invalid score"
            elif score >= EXCELLENT_SCORE:
                result = "Excellent"
            elif score >= PASSABLE_SCORE:
                result = "Passable"
            else:
                result = "Bad"
            print(result)
        elif choice == "S":
            for i in range(score):
                print("*", end="")
            print()
        else:
            print("Invalid")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


main()
