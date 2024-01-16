country_capitals = {"England": "London", "China": "Beijing",
                    "India": "New Delhi", "Russia": "Moscow", "Japan": "Tokyo"}


def find_original_case(country):
    for c in country_capitals:
        if c.lower() == country.lower():
            return c
    return None


def main():
    termination_keyword = "exit"

    while True:
        country = input("Enter the name of a country (or 'exit' to terminate): ").capitalize()

        if country.lower() == termination_keyword.lower():
            break

        original_case_country = find_original_case(country)
        if original_case_country is not None and original_case_country in country_capitals:
            capital = country_capitals[original_case_country]
            print(f"The capital city of {original_case_country} is {capital}")
        else:
            capital = input(f"Enter the capital city of {country}: ").capitalize()
            country_capitals[country] = capital
            print(f"{country} and its capital {capital} have been added to the list.")


if __name__ == "__main__":
    main()
