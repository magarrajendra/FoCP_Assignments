def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def main():
    input_str = input("Enter temperature in centigrade (e.g., 25 C): ")

    try:
        temperature, unit = input_str.split()
        temperature = float(temperature)
    except ValueError:
        print("Invalid input format. Please enter a number followed by a letter C.")
        return

    if unit.lower() != 'c':
        print("Invalid unit. Please enter the temperature in centigrade.")
        return

    fahrenheit_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature} C is equivalent to {fahrenheit_temperature} F.")


main()
