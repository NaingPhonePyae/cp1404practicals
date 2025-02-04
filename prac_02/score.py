"""
Result determining
"""


def main():
    """Result determining program"""
    score = float(input("Enter score: "))
    result = determine_grade(score)
    print(result)


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
