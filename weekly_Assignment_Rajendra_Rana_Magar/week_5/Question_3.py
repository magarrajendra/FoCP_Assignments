import sys


def find_shortest(arguments):
    sorted_arguments = sorted(arguments, key=len)

    shortest = sorted_arguments[0]

    return shortest


if __name__ == "__main__":
    cmd_line_args = sys.argv[1:]

    if not cmd_line_args:
        print("No arguments provided. Please provide at least one argument.")
    else:
        shortest_argument = find_shortest(cmd_line_args)
        print("Shortest argument:", shortest_argument)

