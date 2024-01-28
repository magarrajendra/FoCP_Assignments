password_file = "passwd.txt"


def del_user():
    """Deletes an existing user."""
    username = input("Enter username to delete: ").lower()

    with open(password_file, "r") as file:
        lines = file.readlines()

    user_found = False

    for line in lines:
        parts = line.strip().split(":")
        if not parts[0].lower() == username:
            continue

        user_found = True
        password = input("Confirm deletion (Y/N): ").lower()
        if password in ['y', 'yes']:
            lines.remove(line)
            print(f"User {username} Deleted.")
        else:
            print(f"Deletion canceled.")
            return

    if not user_found:
        print("User not found. Nothing changed.")
        return

    with open(password_file, "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    del_user()
