from my_functions import get_positive_integer_input, get_yes_or_no_input, calculate_price


def main():
    """Main function to run price calculator program."""
    print(" Motu Patlu Pizza House\n"
          "*** Price Calculator ***\n===============================")

    pizza_count = get_positive_integer_input("Total number of pizzas ordered: ")
    delivery_opt = get_yes_or_no_input("Is delivery required? ")
    is_tuesday = get_yes_or_no_input("Is it Tuesday? ")
    used_app = get_yes_or_no_input("Did the customer use the app? ")

    grand_total_price = calculate_price(pizza_count, delivery_opt, is_tuesday, used_app)

    print(f"\nGrand Total Price: £ {grand_total_price:.2f}.")
    print("==============================\nOrder Summary:")
    print(f"Number of Pizzas: {pizza_count}")
    print(f"Need Delivery? {'Yes' if delivery_opt else 'No'}"
          f"{'\n(Eligible for free delivery!)' if pizza_count > 4 else ''}")
    print(f"Tuesday Discount: {'Applied' if is_tuesday else 'Not Applied'}")
    print(f"App Discount: {'Applied' if used_app else 'Not Applied'}")


main()
