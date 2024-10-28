"""
CP1404 Assignment 1 - Travel Tracker
Name:Yik kwokchun
Date started: 20/10/2024
GitHub URL:https://github.com/KwokchunYi/CP1404-Practical
"""

import random

# Constants
FILENAME = "places.csv"
UNVISITED = 'n'
VISITED = 'v'


def main():
    print("Travel Tracker 1.0 - by Your Name")
    places = load_places()
    print(f"{len(places)} places loaded from {FILENAME}")

    while True:
        print(
            "\nMenu:\nD - Display all places\nR - Recommend a random place\nA - Add a new place\nM - Mark a place as visited\nQ - Quit")
        choice = input(">>> ").upper()

        if choice == "D":
            display_places(places)
        elif choice == "R":
            recommend_place(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_visited(places)
        elif choice == "Q":
            save_places(places)
            print(f"{len(places)} places saved to {FILENAME}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def load_places():
    """Load places from CSV file into a list of lists."""
    places = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                name, country, priority, visited = line.strip().split(',')
                places.append([name, country, int(priority), visited])
    except FileNotFoundError:
        print(f"{FILENAME} not found. Starting with an empty list.")
    return places


def save_places(places):
    """Save places to CSV file."""
    with open(FILENAME, "w") as file:
        for place in places:
            file.write(f"{place[0]},{place[1]},{place[2]},{place[3]}\n")


def display_places(places):
    """Display all places sorted by visited status and priority."""
    if not places:
        print("No places to display.")
        return

    places.sort(key=lambda p: (p[3] == VISITED, p[2]))  # Sort by visited status then priority
    max_name_len = max(len(place[0]) for place in places)
    max_country_len = max(len(place[1]) for place in places)

    unvisited_count = sum(1 for place in places if place[3] == UNVISITED)
    for i, place in enumerate(places, 1):
        star = "*" if place[3] == UNVISITED else " "
        print(f"{star}{i}. {place[0]:<{max_name_len}} in {place[1]:<{max_country_len}} {place[2]}")

    print(f"{len(places)} places tracked. You still want to visit {unvisited_count} places.")


def recommend_place(places):
    """Recommend a random unvisited place."""
    unvisited_places = [place for place in places if place[3] == UNVISITED]
    if not unvisited_places:
        print("No places left to visit!")
    else:
        place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {place[0]} in {place[1]}?")


def add_place(places):
    """Add a new place to the list."""
    name = get_nonempty_input("Name: ")
    country = get_nonempty_input("Country: ")
    priority = get_positive_integer("Priority: ")

    places.append([name, country, priority, UNVISITED])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def mark_visited(places):
    """Mark a selected unvisited place as visited."""
    unvisited_places = [place for place in places if place[3] == UNVISITED]
    if not unvisited_places:
        print("No unvisited places")
        return

    display_places(places)
    while True:
        try:
            place_number = int(input("Enter the number of a place to mark as visited\n>>> "))
            if place_number <= 0:
                print("Number must be > 0")
                continue
            if place_number > len(places):
                print("Invalid place number")
                continue
            place = places[place_number - 1]
            if place[3] == VISITED:
                print(f"You have already visited {place[0]}")
            else:
                place[3] = VISITED
                print(f"{place[0]} in {place[1]} visited!")
            break
        except ValueError:
            print("Invalid input; enter a valid number")


def get_nonempty_input(prompt):
    """Get a non-empty string from user."""
    while True:
        response = input(prompt)
        if response.strip():
            return response
        print("Input cannot be blank")


def get_positive_integer(prompt):
    """Get a positive integer from user."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == "__main__":
    main()