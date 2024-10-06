# exceptions_demo.py

"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - A ValueError will occur if the user enters a non-integer value (e.g., a string like "abc" or a float) when prompted for the numerator or denominator.
   
2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError will occur if the user enters 0 as the denominator when attempting to calculate the fraction.
   
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, we can change the code to check if the denominator is 0 before performing the division. If it is 0, we can print a message and handle it gracefully without attempting to divide.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    # Check if the denominator is 0 to avoid ZeroDivisionError
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
    
print("Finished.")
