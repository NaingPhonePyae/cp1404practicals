"""
Result determining
"""

import random


def main():
    """Result determining program"""
    score = float(input("Enter score: "))
    result = determine_grade(score)
    print(result)


def display_random_score():
    """Generates a random score between 0 and 100 and prints the result"""
    print(f"{determine_grade(float(random.randint(0, 100)))}")


def determine_grade(score):
    """Determine grade based on score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
