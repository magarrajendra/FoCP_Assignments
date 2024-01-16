import sys


def count_file_lines(file_path):
    try:
        with open(file_path, 'r') as target_file:
            line_count = 0

            word_count = 0
            char_count = 0

            for line_content in target_file:
                line_count += 1
                word_count += len(line_content.split())
                char_count += len(line_content)

            print(f"Number of Lines: {line_count}")
            print(f"Number of Words: {word_count}")
            print(f"Number of Characters: {char_count}")
    except FileNotFoundError as file_not_found_error:
        print(f"Error: {file_not_found_error}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error! Please enter a file name.")
        sys.exit(1)

    file_path_input = sys.argv[1]
    count_file_lines(file_path_input)
