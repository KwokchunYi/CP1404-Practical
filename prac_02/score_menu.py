def get_valid_score():
    """Get a valid score from the user (0-100 inclusive)."""
    while True:
        try:
            score = int(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def print_result(score):
    """Determine and print the result based on the score."""
    if score >= 90:
        result = "A"
    elif score >= 80:
        result = "B"
    elif score >= 70:
        result = "C"
    elif score >= 60:
        result = "D"
    else:
        result = "F"
    print(f"Your result is: {result}")


def show_stars(score):
    """Print stars corresponding to the score."""
    print('*' * score)


def main():
    """Main function to run the score menu program."""
    print("Welcome to the Score Menu Program!")

    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Choose an option: ").strip().upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell! Thanks for using the Score Menu Program.")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
