"""
Result determining
"""

import random

MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50


def main():
    """Result determining program"""
    score = float(input("Enter score: "))
    result = determine_grade(score)
    print(result)


def display_random_score():
    """Generates a random score between 0 and 100 and prints the result"""
    print(f"{determine_grade(float(random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)))}")


def determine_grade(score):
    """Determine grade based on score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        result = "Invalid score"
    elif score >= EXCELLENT_SCORE:
        result = "Excellent"
    elif score >= PASSABLE_SCORE:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
