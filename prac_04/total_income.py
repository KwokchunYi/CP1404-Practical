"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    months = int(input("How many months? "))
    incomes = []

    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    total = 0
    print_report(total, incomes, months)

def print_report(total, income, num_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        incomes = income[month - 1]
        total += incomes
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()
