import sys


def next_line(file_name):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}\t{line.rstrip()}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error! Please enter a file name.")
        sys.exit(1)

    input_file_name = sys.argv[1]
    next_line(input_file_name)
