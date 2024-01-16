from encryption import rot13
from getpass import getpass

password_file = "passwd.txt"


def login():
    """Gives access to the user if entered correct passwords."""
    username = input("Enter username: ").lower()
    password = getpass("Enter password: ")

    with open(password_file, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if parts[0] == username:
                if parts[2] == rot13(password):
                    print("Access granted.")
                    return
                else:
                    print("Access denied.")
                    return

    print(f"sorry! Username {username} do not exist.")


if __name__ == "__main__":
    login()
