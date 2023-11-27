"""
CP1404/CP5632 - Practical - Suggested Solution
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%,and
a 50% chance that it decreases by 8 to 5%.
If the price rises above $1080, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAXIMUM_INCREASE = 0.175  # 17.5%
MAXIMUM_DECREASE = 0.05  #  5%
MINIMUM_PRICE = 1
MAXIMUM_PRICE = 1000
INITIAL_PRICE = 10.0
OUTPUT_FILE = "capitalist. txt"
number_of_days = 0


price = INITIAL_PRICE
print(f"Starting price : ${price:,.2f}")


out_file = open(OUTPUT_FILE, 'w')
print(f"Starting price : ${price:,.2f}", file=out_file)

while (MINIMUM_PRICE <= price) and (price <= MAXIMUM_PRICE):
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint( a: 1, b: 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform( a:0, MAXIMUM_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price = random.uniform(-MAXIMUM_DECREASE, b:0)
    number_of_days += 1

    price *=(1 + price_change)
    print(f"On day {number_of_days} price is ${price:,.2f}"), file=out_file)
    print(f"On day {number_of_days} price is ${price:,.2f}")
out_file.close()


