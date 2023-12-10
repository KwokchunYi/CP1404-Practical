# guitars.py

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def is_vintage(self):
        return 2023 - self.year >= 50

# Function to input guitars and store them in a list
def get_guitars():
    guitars = []
    while True:
        name = input("Name: ")
        if not name:
            break  # Stop if the user enters a blank name

        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.\n")

    return guitars

# Function to display guitar details
def display_guitars(guitars):
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    print("My guitars!")
    user_guitars = get_guitars()
    display_guitars(user_guitars)
