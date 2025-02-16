"""Questions
1. When will a ValueError occur?
A ValueError will occur when it gets an unexpected value input of the same type
It will also occur when a variable input a value of different type from the expected type

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur the denominator of a fraction is equal to zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You could change by asking a denominator when it is equal to zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator should not be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
