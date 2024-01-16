def get_positive_integer_input(prompt):
    """Only takes positive integer as valid input."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            elif value == 0:
                print("Are you sure! Please confirm the order again.")
            else:
                print("Error! Please enter in a positive integer.")
        except ValueError:
            print("Error! Please enter in a valid number.")


def get_yes_or_no_input(prompt):
    """ Only takes 'yes/no' or 'y/n' input, returns in bool."""
    while True:
        response = input(prompt).lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print('Please answer in "Yes/No" or "Y/N".')


def calculate_price(pizza_count, delivery_opt, is_tuesday, used_app):
    """Calculates total price, applies discounts or charges if conditions are valid."""
    price_per_pizza = 12.00
    delivery_cost = 2.50
    discount_tuesday = 0.50
    discount_app = 0.25

    total_price = price_per_pizza * pizza_count

    if is_tuesday:
        total_price -= total_price * discount_tuesday

    if delivery_opt:
        if pizza_count >= 5:
            total_price += 0  # Free delivery for 5 or more pizzas
        else:
            total_price += delivery_cost

    if used_app:
        total_price -= total_price * discount_app

    return round(total_price, 2)


if __name__ == "__main__":
    print("checking if my_function are working correctly:)")

    test1 = get_positive_integer_input("Order Quantity")
    print(test1)

    test2 = get_yes_or_no_input("Y/N")
    print(test2)

    p_count = 4
    d_opt = True
    is_tue = True
    app = True

    test3 = calculate_price(p_count, d_opt, is_tue, app)
    print(test3)
