import sys


def report_arguments_count():
    """Report the number of command-line arguments provided."""
    arguments_count = len(sys.argv) - 1
    print(f"Number of command-line arguments provided: {arguments_count}")


if __name__ == "__main__":
    report_arguments_count()
