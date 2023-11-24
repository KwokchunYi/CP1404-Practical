MIN_PASSWORD_LENGTH = 10

def main():
    user_password = get_password()
    while len(user_password) < MINI_PASS_LENGTH:
        print("password must be at least(MIN_PASSWORD_LENGTH)long.Try again.")
        user_password = get_password()

    asterisk_password = get_asterisk(password)
    print(asterisk_password)

def get_password():
    user_password = input("please enter a password:")

    return user_password

def get_asterisk(password):
    asterisk_password = ""
    for i in range(len(password)):
        asterisk_password +="*"

    return asterisk_password



