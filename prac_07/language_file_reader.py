import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = read_languages("languages.csv")

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


def read_languages(filename):
    """Read programming languages from a file and return a list of objects."""
    languages = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            parts = line.strip().split(',')
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"  # New field for pointer arithmetic
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
            languages.append(language)
    return languages



def using_csv():
    """Language file reader version using the csv module."""
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        for row in reader:
            print(row)


def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        print(file_field_names)
        # Updated to include pointer_arithmetic
        Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
        reader = csv.reader(in_file)
        for row in reader:
            row[2] = row[2] == "Yes"  # Convert reflection to Boolean
            row[4] = row[4] == "Yes"  # Convert pointer_arithmetic to Boolean
            language = Language._make(row)
            print(repr(language))


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    # Updated to include pointer_arithmetic
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    with open("languages.csv", "r") as in_file:
        in_file.readline()
        for language in map(lambda row: Language(row[0], row[1], row[2] == "Yes", int(row[3]), row[4] == "Yes"),
                            csv.reader(in_file)):
            print(language.name, 'was released in', language.year)
            print(repr(language))


main()
