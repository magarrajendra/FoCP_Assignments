from encryption import rot13
from getpass import getpass

password_file = "passwd.txt"


def add_user():
    """Adds only new users to the database."""
    while True:
        username = input("Enter new username: ").lower()

        with open(password_file, "r") as file:
            if any(line.startswith(username + ":") for line in file):
                print("Username already exists. Please choose a different username.")
                continue

        real_name = input("Enter your full name: ")

        while True:
            new_password = getpass("Enter your new password: ")
            confirm_password = getpass("Confirm your new password: ")

            if new_password == confirm_password:
                print("Password Set!")
                break
            else:
                print("Error! Passwords do not match. Try again.")

        with open(password_file, "a") as file:
            encrypted_password = rot13(confirm_password)
            file.write(f"{username}:{real_name}:{encrypted_password}\n")

        print(f"User {username} created successfully.")
        break


if __name__ == "__main__":
    add_user()
