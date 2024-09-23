"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Start the loop to repeatedly ask for sales
sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.10  # 10% bonus for sales under $1000
    else:
        bonus = sales * 0.15  # 15% bonus for sales $1000 and over

    print(f"Bonus: ${bonus:.2f}")

    # Get the next sales input
    sales = float(input("Enter sales: $"))

print("Sales entered were negative, exiting the program.")
