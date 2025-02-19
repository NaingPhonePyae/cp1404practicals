"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """print class details from file program"""
    data = load_data()
    for detail in data:
        name_format = max([len(detail[1]) for detail in data])
        student_format = max(len(str(detail[2])) for detail in data)
        print(f"{detail[0]} is taught by {(detail[1]):<{name_format}} and has {(detail[2]):>{student_format}} "
              f"students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME, "r")
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append([part for part in parts])  # Modified part
        print("----------")
    input_file.close()
    return data


main()
