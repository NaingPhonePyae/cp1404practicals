"""
Program to manage project
Expected time: 1 hour
Actual time:
"""
import datetime
from project import Project

COMPLETION_INDEX = 4
COST_INDEX = 3
PRIORITY_INDEX = 2
DATE_INDEX = 1
NAME_INDEX = 0

FILENAME = "test.txt"

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
        elif choice == "F":
            filter_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_projects(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print(f"Would you like to save to {FILENAME}? no, I think not.")
    print("Thank you for using custom-built project management software.")


def update_projects(projects):
    """Update project details"""
    for index, project in enumerate(projects):
        print(index, project)
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_completion = int(input("New percentage: "))
    new_priority = int(input("New priority: "))
    projects[project_choice].completion = new_completion
    projects[project_choice].priority = new_priority
    print(projects[project_choice])


def add_project(projects):
    """Add new project to the list"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: "))
    completion = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost, completion)
    projects.append(project)


def filter_by_date(projects):
    """Filter and display projects that start after input date"""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        project_date = datetime.datetime.strptime(project.date, "%d/%m/%Y").date()
        if project_date >= date:
            print(project)


def display_projects(projects):
    """Display projects according to completion"""
    print("Incomplete projects: ")
    for project in projects:
        if not project.is_completed():
            print(f"  {project}")
    print("Completed projects: ")
    for project in projects:
        if project.is_completed():
            print(f"  {project}")
    print(f"Loaded {len(projects)} projects from projects.txt")


def process_file(projects, filename=FILENAME, process_type="r", choice="L"):
    """process file according to inputs"""
    in_file = open(filename, process_type)
    if choice == "S":
        for project in projects:
            in_file.write(f"{project.name}\t{project.date}\t{project.priority}\t{project.cost}\t{project.completion}\n")
    else:
        for line in in_file:
            parts = line.strip().split("	")
            project = Project(parts[NAME_INDEX], parts[DATE_INDEX], parts[PRIORITY_INDEX], parts[COST_INDEX],
                              int(parts[COMPLETION_INDEX]))
            projects.append(project)
        projects.sort()
    in_file.close()


if __name__ == '__main__':
    main()
