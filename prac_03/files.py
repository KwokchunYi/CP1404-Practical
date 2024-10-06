# files.py

# Task 1: Ask the user for their name and write it to name.txt
name = input("Enter your name: ")
file = open('name.txt', 'w')  # Open the file in write mode
file.write(name)  # Write the name to the file
file.close()  # Close the file

# Task 2: Read the name from name.txt and print a greeting
file = open('name.txt', 'r')  # Open the file in read mode
name_from_file = file.readline().strip()  # Read the name and strip any extra whitespace/newlines
file.close()  # Close the file
print(f"Hi {name_from_file}!")  # Print the greeting

# Task 3: Open numbers.txt and read only the first two numbers, adding them together
# Create the numbers.txt file first
with open('numbers.txt', 'w') as num_file:
    num_file.write("17\n42\n400\n")  # Write the three numbers to the file

# Read the first two numbers
with open('numbers.txt', 'r') as num_file:
    first_number = int(num_file.readline().strip())  # Read the first line and convert to int
    second_number = int(num_file.readline().strip())  # Read the second line and convert to int
    result = first_number + second_number  # Add the two numbers
    print(result)  # Print the result, which should be 59

# Task 4: Print the total for all lines in numbers.txt
with open('numbers.txt', 'r') as num_file:
    total = 0  # Initialize a variable to hold the total
    for line in num_file:  # Iterate through each line in the file
        total += int(line.strip())  # Convert the line to an int and add to total
    print(total)  # Print the total for all numbers
