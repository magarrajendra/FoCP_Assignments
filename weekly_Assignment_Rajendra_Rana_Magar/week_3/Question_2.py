new_password = input("Enter your new password: ")
confirm_password = input("Confirm your new password: ")

if new_password == confirm_password:
    print("Password Set!")
else:
    print("Error! Passwords do not match.")
