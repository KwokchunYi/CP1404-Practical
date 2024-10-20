"""
Emails to Names
Estimate: 30 minutes
Actual: 35 minutes
"""


def get_name_from_email(email):
    """Extracts and returns a name from the email."""
    email_username = email.split('@')[0]
    name_parts = email_username.split('.')
    name = " ".join(name_parts).title()
    return name


# Dictionary to store emails and names
email_to_name = {}

# Get emails and names from the user
email = input("Email: ")
while email != "":
    name = get_name_from_email(email)
    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

    # If the user says no or enters a custom name, prompt for a new name
    if confirmation != "" and confirmation != "y":
        name = input("Name: ")

    # Store the email and name in the dictionary
    email_to_name[email] = name

    # Ask for the next email
    email = input("Email: ")

# Output the stored names and emails
for email, name in email_to_name.items():
    print(f"{name} ({email})")
