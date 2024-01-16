def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


if __name__ == "__main__":
    def main():
        temperatures = []

        while True:
            input_str = input("Enter temperature in centigrade (or press Enter to finish): ")

            if not input_str:
                break

            try:
                temperature, unit = input_str.split()
                temperature = float(temperature)
            except ValueError:
                print("Invalid input format. Please enter a number followed by a letter C.")
                return

            if unit.lower() != 'c':
                print("Invalid unit. Please enter the temperature in centigrade.")
                return

            temperatures.append(temperature)

        if not temperatures:
            print("No temperatures entered.")
            return

        fahrenheit_temperatures = [celsius_to_fahrenheit(temp) for temp in temperatures]

        max_temp = max(fahrenheit_temperatures)
        min_temp = min(fahrenheit_temperatures)
        mean_temp = sum(fahrenheit_temperatures) / len(fahrenheit_temperatures)

        print(f"Maximum temperature: {max_temp:.2f} F")
        print(f"Minimum temperature: {min_temp:.2f} F")
        print(f"Mean temperature: {mean_temp:.2f} F")


    main()

