# menus.py

# Get the user's name
name = input("Enter name: ")

# Display the menu and get the user's choice
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice = input(">>> ").upper()

# Main loop for the menu-driven program
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Display the menu and get the next choice
    print(menu)
    choice = input(">>> ").upper()

# Final message after quitting
print("Finished.")
