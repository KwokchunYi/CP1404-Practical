# Basic list operations
def main():
    # Part 1: Getting 5 numbers from the user
    numbers = []
    for i in range(5):
        number = float(input(f"Enter number {i + 1}: "))  # Prompt for numbers
        numbers.append(number)  # Add number to the list

    # Outputting information about the numbers
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

    # Part 2: Woefully inadequate security checker
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
        'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
        'Command', 'ExecState', 'InteractiveConsole',
        'InterpreterInterface', 'StartServer', 'bob'
    ]

    username = input("Enter your username: ")  # Prompt for username
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
