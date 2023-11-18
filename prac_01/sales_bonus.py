"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
from webbrowser import get

while True:
    sales = float(input("Enter sales: $"))

    if sales < 0:
        break #Exit the loop if the user enters a negative number.

    if sales < 1000:
            bonus = sales * 0.10
    else:
            bonus = sales * 0.15

    print(f"Bonus: ${bonus:.2f}")

