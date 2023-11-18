def get_valid_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Invalid number of items!")
            return value
        except ValueError as e:
            print(e)

def main():
    # Get the number of items
    num_items = get_valid_number("Number of items: ")

    # Initialize total price
    total_price = 0

    # Get the price of each item
    for i in range(num_items):
        while True:
            try:
                price = float(input("Price of item {}: ".format(i + 1)))
                if price < 0:
                    raise ValueError("Invalid price!")
                total_price += price
                break
            except ValueError as e:
                print(e)

    # Apply discount if total price is over $100
    if total_price > 100:
        discount = 0.1 * total_price
        total_price -= discount

    # Display the result with 2 decimal places for currency
    print("Total price for {} items is ${:.2f}".format(num_items, total_price))

if __name__ == "__main__":
    main()


