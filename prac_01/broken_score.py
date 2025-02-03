"""
The intention is that the score must be between 0 and 100 inclusive; 90 or more is excellent; 50 or more is a pass;
below 50 is bad. There is no intention to do any repetition.
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    result = "Invalid score"
elif score >= 90:
    result = "Excellent"
elif score >= 50:
    result = "Passable"
else:
    result = "Bad"
print(result)
