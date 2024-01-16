def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    test_number = int(input("Enter any number to check a prime number: "))
    result = is_prime(test_number)
    print(f"{test_number} is {"prime" if result else "not prime"} number.")
