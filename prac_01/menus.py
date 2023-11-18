def main():
    # Get user's name
    name = input("Enter your name: ")

    # Display menu
    MENU = """Menu:
    H - Say Hello
    G - Say Goodbye
    Q - Quit"""

    print(MENU)
    choice = input("Enter your choice (H, G, or Q): ").upper()

    # Menu-driven loop
    while choice != "Q":
        if choice == "H":
            print("Hello, {}!".format(name))
        elif choice == "G":
            print("Goodbye, {}!".format(name))
        else:
            print("Invalid choice. Please enter H, G, or Q.")

        # Display menu and get choice again
        print(MENU)
        choice = input("Enter your choice (H, G, or Q): ").upper()

    # Display finished message
    print("Program finished. Goodbye, {}!".format(name))

if __name__ == "__main__":
    main()
