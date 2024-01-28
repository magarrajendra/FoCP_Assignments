def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def process_temperatures(celsius_temperatures):
    if not celsius_temperatures:
        print("No temperatures entered.")
        return

    fahrenheit_temperatures = [celsius_to_fahrenheit(temp) for temp in celsius_temperatures]

    max_temp = max(fahrenheit_temperatures)
    min_temp = min(fahrenheit_temperatures)
    mean_temp = sum(fahrenheit_temperatures) / len(fahrenheit_temperatures)

    print(f"Maximum temperature: {max_temp:.2f} F")
    print(f"Minimum temperature: {min_temp:.2f} F")
    print(f"Mean temperature: {mean_temp:.2f} F")


if __name__ == "__main__":
    import sys

    celsius_values = sys.argv[1:]

    if not celsius_values:
        print("No temperatures entered.")
    else:
        try:
            celsius_temp = [float(temp) for temp in celsius_values]
            process_temperatures(celsius_temp)
        except ValueError:
            print("Invalid input. Please provide numerical temperature values.")
