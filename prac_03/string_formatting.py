"""
CP1404/CP5632 - Practical
"""

name = "Gibson L-5 CES"
year = 1992
cost = 16035.4

# The 'old' manual way to format text with string concatenation:
print("My guitar: " + name + ", first made in " + str(year))
print()

# A better way - using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))
print()

# And with f-string formatting (introduced in Python 3.6)
print(f"My {name} was first made in {year} (that's right, {year}!)")
print()

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}")
print()

# Aligning columns by using width after the :
# This loop uses enumerate, useful when you want both the index and value
numbers = [1, 19, 123, 456, -25]
print()

for i, number in enumerate(numbers, 1):
    print(f"Number{i} is {number:5}")

print()
# TODO:Use f-string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,035!
print(f"{year} {name} for about ${cost:,.0f}!")
print()

# TODO: Using a for loop with the range function and string formation,
# produce the following right-aligned output:
#   0
#   50
#   100
#   150

for i in range(0, 151, 50):
    print(f"{i:>3}")  # alight to the right

print()

for i in range(0, 151, 50):
    print(f"{i:<3}")  # alight to the left

print()

for i in range(0, 151, 50):
    print(f"{i:^3}")   # alight to the center

print()