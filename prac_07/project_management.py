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
    """"""
    print("Welcome to Pythonic Project Management")
    projects = []
    process_file(projects, FILENAME)
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            process_file(projects, filename)
        elif choice == "S":
            filename = input("Filename: ")
            process_type = input("Reading type (a/ w/ r): ")
            process_file(projects, filename, process_type, choice)
        elif choice == "D":
            display_projects(projects)
        # elif choice == "F":
        #
        # elif choice == "A":
        #
        # elif choice == "U":

        else:
            print("Invalid choice")
        # print(MENU)
        choice = input(">>> ").upper()

    print(f"Would you like to save to {FILENAME}? no, I think not.")


def display_projects(projects):
    """Display projects according to completion"""
    print("Incomplete projects: ")
    for project in projects:
        if not project.is_completed():
            print(project)
    print("Completed projects: ")
    for project in projects:
        if project.is_completed():
            print(project)
    print(f"Loaded {len(projects)} projects from projects.txt")


def process_file(projects, filename, process_type="r", choice="L"):
    """process file according to inputs"""
    in_file = open(filename, process_type)
    if choice == "S":
        for project in projects:
            in_file.write(f"{project.name}\t{project.date}\t{project.priority}\t{project.cost}\t{project.completion}\n")
    else:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("	")
            project = Project(parts[NAME_INDEX], parts[DATE_INDEX], parts[PRIORITY_INDEX], parts[COST_INDEX],
                              int(parts[COMPLETION_INDEX]))
            projects.append(project)
        projects.sort()
    in_file.close()


if __name__ == '__main__':
    main()
