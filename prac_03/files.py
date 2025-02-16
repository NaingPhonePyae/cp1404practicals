"""
Make the appropriate choice of file-reading technique for each of these questions:
read()
readline()
readlines()
for line in file
"""

NAME_FILE = "name.txt"
NUMBER_FILE = "numbers.txt"

# 1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
name = input("Name: ")
out_file = open(NAME_FILE, "w")
print(name, file=out_file)
out_file.close()

# 2. In the same file, but as if it were a separate program, write code that opens "name.txt"
# and reads the name (as above) then prints (note the exact output),
in_file = open(NAME_FILE, "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.Write code that opens numbers.txt, reads only the first two numbers, adds them together
# then prints the result, which should be... 59. Use with instead of open and close for this question.
with open(NUMBER_FILE, "r") as in_file:
    first_number = int(in_file.readline().strip())
    second_number = int(in_file.readline().strip())
    print(first_number + second_number)

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt.
total = 0
with open(NUMBER_FILE, "r") as in_file:
    numbers = in_file.readlines()
    for number in numbers:
        total += int(number.strip())
    print(total)
