import sys


def report_platform():
    """Reports the operating system platform."""
    platform = sys.platform
    print(f"The operating system platform is: {platform}")


if __name__ == "__main__":
    report_platform()
