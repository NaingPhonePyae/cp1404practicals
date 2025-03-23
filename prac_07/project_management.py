"""
Program to manage project
Expected time: 1 hour
Actual time:
"""

from project import Project

COMPLETION_INDEX = 4
COST_INDEX = 3
PRIORITY_INDEX = 2
DATE_INDEX = 1
NAME_INDEX = 0

FILENAME = "projects.txt"

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    print("Welcome to Pythonic Project Management")
    projects = []
    process_file(projects)

    print(f"Loaded {len(projects)} projects from projects.txt")
    projects.sort()

    print(MENU)

    # choice = input(">>> ").upper()
    # while choice != "Q":
    #     # if choice == "L":
    #     #
    #     # elif choice == "S":
    #     #
    #     # elif choice == "D":
    #     #
    #     # elif choice == "F":
    #     #
    #     # elif choice == "A":
    #     #
    #     # elif choice == "U":
    #
    #     else:
    #         print("Invalid choice")
    #
    #     choice = input(">>> ").upper()
    #
    # print(f"Would you like to save to {FILENAME}? no, I think not.")


def process_file(projects, filename=FILENAME, process_type="r", choice="L"):
    in_file = open(filename, process_type)
    if choice == "L":
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("	")
            project = Project(parts[NAME_INDEX], parts[DATE_INDEX], parts[PRIORITY_INDEX], parts[COST_INDEX],
                              int(parts[COMPLETION_INDEX]))
            print(project)
            projects.append(project)
    else:
        for project in projects:
            in_file.write(project)
    in_file.close()


if __name__ == '__main__':
    main()
