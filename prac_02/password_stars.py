def get_password():
    """Get a password from the user and check its validity."""
    password = input("Enter your password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return get_password()  # Recursive call to get a valid password
    return password

def print_asterisks(password):
    """Print asterisks corresponding to the length of the password."""
    print('*' * len(password))

def main():
    """Main function to run the password check program."""
    password = get_password()
    print_asterisks(password)

if __name__ == "__main__":
    main()
