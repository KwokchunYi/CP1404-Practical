import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    # Ask the user how many quick picks they want
    num_picks = int(input("How many quick picks? "))

    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in sorted(quick_pick)))

def generate_quick_pick():
    """Generate a single quick pick of 6 unique random numbers."""
    quick_pick = set()  # Use a set to avoid duplicates
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.add(number)  # Add the number to the set
    return list(quick_pick)  # Convert set to list to return

main()
