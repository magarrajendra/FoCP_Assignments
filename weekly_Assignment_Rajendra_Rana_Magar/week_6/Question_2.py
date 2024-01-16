def find_factors(num):
    if num < 1:
        raise ValueError("Input must be a positive integer")

    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors


if __name__ == "__main__":
    find_factors_of = 12
    factors_result = find_factors(find_factors_of)
    print(f"The factors of {find_factors_of} are: {factors_result}")

