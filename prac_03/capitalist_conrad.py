"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

# Constants for the simulation
MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

# Initialize price and day counter
price = INITIAL_PRICE
number_of_days = 0

# Print the initial price
print(f"Starting price: ${price:,.2f}")

# Run the simulation
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1  # Increment day count
    price_change = 0

    # Generate a random integer (1 or 2) to determine increase or decrease
    if random.randint(1, 2) == 1:
        # Price increases
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Price decreases
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Update the price based on the change
    price *= (1 + price_change)

    # Print the price for the day
    print(f"On day {number_of_days}, price is: ${price:,.2f}")

# Print final result after the loop ends
print(f"Simulation ended after {number_of_days} days.")

