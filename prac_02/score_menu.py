
# (G)et a valid score (must be 0-100 inclusive)
# (P)rint result (copy or import your function to determine the result from score.py)
# (S)how stars (this should print as many stars as the score)
# (Q)uit
def get_valid_score():
    while True:
        score = input("Enter a valid score (0-100 inclusive): ")
        if score.isdigit() and 0 <= int(score) <= 100:
            return int(score)
        else:
            print("Invalid score! Please try again.")


def print_result(score):
    # Copy or import your function from score.py to determine the result
    # Replace the print statement below with the appropriate function call
    print(f"The result for score {score} is ...")


def show_stars(score):
    print("*" * score)


def main():
    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            break
        else:
            print("Invalid choice! Please try again.")

    print("Farewell!")


if __name__ == "__main__":
    main()