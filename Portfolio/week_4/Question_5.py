def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


if __name__ == "__main__":

    celsius_temperature = 37.5
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
    print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")

    fahrenheit_temperature = 68.0
    celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
    print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature} degrees Celsius.")
