"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)  # Call the new function to display details


def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    subjects = []  # List to hold subject data
    input_file = open(FILENAME)

    for line in input_file:
        line = line.strip()  # Remove the newline character
        parts = line.split(',')  # Split the line into its parts
        parts[2] = int(parts[2])  # Convert the number of students to an integer
        subjects.append(parts)  # Add the parts to the subjects list

    input_file.close()
    return subjects  # Return the list of subjects


def display_subject_details(subjects):
    """Display subject details in the specified format."""
    for subject in subjects:
        code, lecturer, num_students = subject
        print(f"{code} is taught by {lecturer} and has {num_students} students.")


# Entry point of the program
if __name__ == "__main__":
    main()
