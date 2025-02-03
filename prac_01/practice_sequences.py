"""
1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program
"""

MENU = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program
"""
x_value = int(input("starting value: "))
y_value = int(input("last value: "))
while x_value > y_value:
    print("Last value should be greater than starting value")
    x_value = int(input("starting value: "))
    y_value = int(input("last value: "))
print(MENU)
choice = input(">>> ")
while choice != "4":
    if choice == "1":
        x = x_value
        if x % 2 != 0:
            x += 1
        for number in range(x, y_value + 1, 2):
            print(number, end=" ")
        print()
    elif choice == "2":
        x = x_value
        if x % 2 == 0:
            x += 1
        for number in range(x, y_value + 1, 2):
            print(number, end=" ")
        print()
    elif choice == "3":
        for number in range(x_value, y_value + 1):
            print(number ** 2, end=" ")
        print()
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ")
print("Done")
