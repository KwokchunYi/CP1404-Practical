"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MINIMUM_LENGTH = 5
MAXIMUM_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "10#$%^&*).-=+`~,./'[]<>?{}|\\"


def mainO:
    """Validate password."""
    print ("Please enter a valid password")
    print("Your password must be between", MINIMUM_LENGTH, "and", MAXIMUM_LENGTH,
        "characters, and contain:")
    print("\t or more uppercase characters")
    print("\t or more lowercase characters")
    print("\t or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid:{password}")


def is_valid_password(password):
    """ Validate password length."""
    # TODO: if legnth is wrong, return False
    if len(password) < MINIMUM_LENGTH or len(password) > MINIMUM_LENGTH:
        print(f"Password must be between {MINIMUM_LENGTH} and {MAXIMUM_LENGTH}")
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like is digit)
        if char.isdigit():
            count_digit += 1
        elif char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1
        else:
            pass

    # TODO: if any of the 'normal' counts are zero, return False
    if count_lower < 1 or count_upper < 1 or count_digit < 1:
        return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if SPECIAL_CHARS_REQUIRED:
        if count_special ==0:
            return False

        # if we get here (without returning False), then the password must be valid
        return True


mainO()




