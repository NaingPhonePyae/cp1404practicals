"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

pseudocode
get sales
if sales > 1000
    bonus_rate = 0.15
else
    bonus_rate = 0.1
bonus_amount = sales * bonus_rate
print bonus_amount
"""

sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus_rate = 0.1
else:
    bonus_rate = 0.15
bonus_amount = sales * bonus_rate
print(f"The bonus is ${bonus_amount:.2f}")


# repeatedly asks for the user's sales and prints the bonus until they enter a negative number
sales = float(input("Enter sales: $"))
bonus_amount = 0
while sales >= 0:
    if sales < 1000:
        bonus_rate = 0.1
    else:
        bonus_rate = 0.15
    bonus_amount += sales * bonus_rate
    sales = float(input("Enter sales: $"))
print(f"The bonus is ${bonus_amount:.2f}")
