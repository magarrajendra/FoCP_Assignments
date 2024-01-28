def is_valid_integer(num):
    """Checks if the given number is an integer within the range 0 to 100 (inclusive)."""
    return 0 <= num <= 100


if __name__ == "__main__":
    test_inputs = [42, -5, 101, 5, 99, 100, 0]

    for i in test_inputs:
        print(f"{i} is in the range 0 to 100: {is_valid_integer(i)}")
