from guitar import Guitar
import csv
def read_guitars_from_file(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Skip any empty rows
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display all guitars in the list."""
    for guitar in guitars:
        print(guitar)

def sort_guitars_by_year(guitars):
    """Sort the list of guitars by year (oldest to newest)."""
    guitars.sort()  # This will use the __lt__ method in Guitar class

def add_new_guitars(guitars):
    """Prompt the user to enter new guitars and add them to the list."""
    while True:
        name = input("Enter guitar name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        year = int(input("Enter the year of the guitar: "))
        cost = float(input("Enter the cost of the guitar: $"))
        guitars.append(Guitar(name, year, cost))

def save_guitars_to_file(filename, guitars):
    """Write the list of guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    """Main function to run the guitar program."""
    filename = "guitars.csv"

    # Read guitars from file
    guitars = read_guitars_from_file(filename)

    # Display all guitars
    print("All Guitars:")
    display_guitars(guitars)

    # Sort guitars by year
    sort_guitars_by_year(guitars)
    print("\nSorted Guitars (by Year):")
    display_guitars(guitars)

    # Add new guitars
    add_new_guitars(guitars)

    # Save updated list back to file
    save_guitars_to_file(filename, guitars)
    print("\nUpdated list of guitars saved to file.")


if __name__ == "__main__":
    main()
