"""
CP1404 - Practical
Answer the following  questions:
1. When will a ValueError occur?
when Numerator and denominator are not valid numbers

2.  When will a ZeroDivisionError occur?
when denominator are 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("Cannot divide by zero!")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except  ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")


