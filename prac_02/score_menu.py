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
    score = valid_score(score)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Score: "))
            score = valid_score(score)
        elif choice == "P":
            result = determine_grade(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def print_stars(score):
    for i in range(score):
        print("*", end="")
    print()


def determine_grade(score):
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        result = "Invalid score"
    elif score >= EXCELLENT_SCORE:
        result = "Excellent"
    elif score >= PASSABLE_SCORE:
        result = "Passable"
    else:
        result = "Bad"
    return result


def valid_score(score):
    while score not in range(MINIMUM_SCORE, MAXIMUM_SCORE + 1):
        print("Invalid score")
        score = int(input("Score: "))
    return score


main()
