from encryption import rot13
from getpass import getpass

password_file = "passwd.txt"


def change_password():
    """Changes current passwords if entered correctly."""
    username = input("Enter your username: ").lower()

    with open(password_file, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        parts = line.strip().split(":")
        if parts[0].lower() == username:
            current_password = getpass("Enter your current password: ")
            encrypted_current_password = rot13(current_password)

            if encrypted_current_password == parts[2]:
                new_password = getpass("Enter your new password: ")
                confirm_password = getpass("Confirm your new password: ")

                if new_password == confirm_password:
                    encrypted_new_password = rot13(new_password)
                    lines[i] = f"{username}:{parts[1]}:{encrypted_new_password}\n"
                    with open(password_file, "w") as file:
                        file.writelines(lines)
                        print("Password changed successfully.")
                    return
                else:
                    print("Error! Passwords do not match. Password change canceled.")
                    return
            else:
                print("Incorrect current password. Password change canceled.")
                return

    print("Username not found. Password change canceled.")


if __name__ == "__main__":
    change_password()
