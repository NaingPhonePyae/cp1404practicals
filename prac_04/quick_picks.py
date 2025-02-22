"""
Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many
lines of output. Each line consists of 6 random numbers between 1 and 45.These values should be stored as CONSTANTS.

Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Study the formatting below so that numbers align neatly.
"""

import random

MAXIMUM = 45
MINIMUM = 1
WORD_PER_LINE = 6

maximum_length = len(str(MAXIMUM))
is_valid = False
while not is_valid:
    try:
        quick_picks = int(input("How many picks? "))
        while quick_picks <= 0:
            print("Nothing to display")
            quick_picks = int(input("How many picks? "))
        for i in range(quick_picks):
            numbers = []
            for j in range(WORD_PER_LINE):
                number = random.randint(MINIMUM, MAXIMUM)
                while number in numbers:
                    number = random.randint(MINIMUM, MAXIMUM)
                numbers.append(number)
            numbers.sort()
            print(" ".join(f"{number:>{maximum_length}}" for number in numbers), end="")
            print()
        is_valid = True
    except ValueError:
        print("Put a valid value")

