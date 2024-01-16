number = int(input("Enter number between 0 and 12 to generate times table: "))

if not 0 <= number <= 12:
    print("Invalid input! Please enter a number between 0 and 12.")
else:
    print(f"Generating the times table for: {number}")

    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")
