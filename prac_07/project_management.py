import os
from project import Project


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()  # Skip header
            for line in file:
                parts = line.strip().split('\t')
                name = parts[0]
                completion_percentage = int(parts[1])
                priority = int(parts[2])
                start_date = parts[3]
                projects.append(Project(name, completion_percentage, priority, start_date))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty project list.")
    return projects


def save_projects(filename, projects):
    """Save the list of projects to a file."""
    with open(filename, 'w') as file:
        file.write("Project Name\tCompletion %\tPriority\tStart Date\n")
        for project in projects:
            file.write(f"{project.name}\t{project.completion_percentage}\t{project.priority}\t{project.start_date}\n")


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = [p for p in projects if p.completion_percentage < 100]
    completed = [p for p in projects if p.completion_percentage == 100]

    print("\nIncomplete Projects:")
    for project in sorted(incomplete):
        print(project)

    print("\nCompleted Projects:")
    for project in sorted(completed):
        print(project)


def filter_projects_by_date(projects, date):
    """Filter and display projects that start after the given date."""
    filtered_projects = [p for p in projects if p.start_date > date]
    print(f"\nProjects starting after {date}:")
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


def add_new_project(projects):
    """Add a new project to the project list."""
    name = input("Enter project name: ")
    completion_percentage = int(input("Enter completion percentage (0-100): "))
    priority = int(input("Enter priority (1 = highest): "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    project = Project(name, completion_percentage, priority, start_date)
    projects.append(project)


def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    display_projects(projects)
    project_name = input("\nEnter the project name to update: ")
    project = next((p for p in projects if p.name.lower() == project_name.lower()), None)

    if project:
        new_completion = input(
            f"Enter new completion percentage for {project.name} (current: {project.completion_percentage}): ")
        new_priority = input(f"Enter new priority for {project.name} (current: {project.priority}): ")

        if new_completion:
            project.completion_percentage = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)
    else:
        print(f"Project '{project_name}' not found.")


def main():
    """Main function to run the project management program."""
    filename = "projects.txt"
    projects = load_projects(filename)

    while True:
        print("\nMenu:")
        print("1. Load projects")
        print("2. Save projects")
        print("3. Display projects")
        print("4. Filter projects by date")
        print("5. Add new project")
        print("6. Update project")
        print("7. Quit")

        choice = input("Enter choice (1-7): ")

        if choice == '1':
            load_filename = input("Enter filename to load: ")
            projects = load_projects(load_filename)
        elif choice == '2':
            save_filename = input("Enter filename to save: ")
            save_projects(save_filename, projects)
        elif choice == '3':
            display_projects(projects)
        elif choice == '4':
            date = input("Enter date (YYYY-MM-DD): ")
            filter_projects_by_date(projects, date)
        elif choice == '5':
            add_new_project(projects)
        elif choice == '6':
            update_project(projects)
        elif choice == '7':
            save_choice = input("Would you like to save your changes? (y/n): ")
            if save_choice.lower() == 'y':
                save_projects(filename, projects)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
