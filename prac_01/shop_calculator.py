# shop_calculator.py

# Get number of items with input validation
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Calculate the total price
total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply discount if total price is over $100
if total_price > 100:
    total_price *= 0.9  # Apply 10% discount

# Display the total price, formatted to 2 decimal places
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
