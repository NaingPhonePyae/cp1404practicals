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
    random_score = generate_random_score(MINIMUM_SCORE, MAXIMUM_SCORE + 1)
    print(f"{random_score:.1f} is {determine_grade(random_score)}")


def generate_random_score(low, high):
    """Generates a random score between low and high"""
    return random.randrange(low, high)


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
