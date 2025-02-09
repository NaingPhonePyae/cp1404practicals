"""Score menu"""

MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

MENU = ("(G)et a valid score\n"
        "(P)rint result\n"
        "(S)how stars\n"
        "(Q)uit")


def main():
    """Score menu program"""
    score = get_valid_score(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(MINIMUM_SCORE, MAXIMUM_SCORE)
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
    """print stars according to score"""
    for i in range(score):
        print("*", end="")
    print()


def determine_grade(score):
    """determine grade based on score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        result = "Invalid score"
    elif score >= EXCELLENT_SCORE:
        result = "Excellent"
    elif score >= PASSABLE_SCORE:
        result = "Passable"
    else:
        result = "Bad"
    return result


def get_valid_score(low, high):
    """get valid input score"""
    score = int(input("Score: "))
    while score < low or score > high:
        print("Invalid score")
        score = int(input("Score: "))
    return score


main()
