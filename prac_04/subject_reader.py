"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    for line in data:
        print(f"{line[0]} is taught by {line[1]} and has {line[1]} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts) # Append the parts to the data list
    input_file.close()
    return data

def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        code, teacher, students = subject
        print(f'{code} is taught by {teacher} and has {students} students')


if __name__ == "__main__":
    main()