# randoms.py

import random

# Line 1: Generate a random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))  # This will print a random integer between 5 and 20

# What did you see on line 1?
# The output is a random integer between 5 and 20, inclusive.
# What was the smallest number you could have seen, what was the largest?
# The smallest number could have been 5 and the largest number could have been 20.

# Line 2: Generate a random number from a range, starting from 3 up to (but not including) 10, with a step of 2
print(random.randrange(3, 10, 2))  # This will print a random number in {3, 5, 7, 9}

# What did you see on line 2?
# The output is a random number selected from the set {3, 5, 7, 9}.
# What was the smallest number you could have seen, what was the largest?
# The smallest number could have been 3 and the largest number could have been 9.
# Could line 2 have produced a 4?
# No, line 2 could not have produced a 4 because it only selects odd numbers from the specified range.

# Line 3: Generate a random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # This will print a random float between 2.5 and 5.5

# What did you see on line 3?
# The output is a random floating-point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# The smallest number could have been 2.5 and the largest number could have been 5.5.

# Generate a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)  # This will print a random integer between 1 and 100 inclusive.
