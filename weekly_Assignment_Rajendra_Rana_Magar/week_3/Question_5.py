BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    new_password = input("Enter your new password: ")

    if new_password.lower() in BAD_PASSWORDS:
        print("Error! Entered password is commonly used. Try new password.\n")
    elif not 8 <= len(new_password) <= 12:
        print("Error! Password must be between 8 and 12 characters.\n")
    else:
        confirm_password = input("Confirm your new password: ")

        if new_password == confirm_password:
            print("Password Set!")
            break
        else:
            print("Error! Passwords do not match. Try again.\n")
