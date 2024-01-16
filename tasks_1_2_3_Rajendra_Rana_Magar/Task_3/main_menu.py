from add_user import add_user
from del_user import del_user
from change_password import change_password
from login import login


def main_menu():
    """Main program starts here."""
    while True:
        print("\n=== Main Menu:===")
        print("1. Add New User")
        print("2. Delete User")
        print("3. Change Password")
        print("4. Login")
        print("5. Exit")

        choice = input("Enter your selection (1-5): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            del_user()
        elif choice == "3":
            change_password()
        elif choice == "4":
            login()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main_menu()
