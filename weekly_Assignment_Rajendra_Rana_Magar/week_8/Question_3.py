import sys


def grep_search(search_term, file_to_search):
    try:
        with open(file_to_search, 'r') as search_file:
            search_term_lower = search_term.lower()
            found_occurrence = False
            for line_in_file in search_file:
                if search_term_lower in line_in_file.lower():
                    print(line_in_file.rstrip())
                    found_occurrence = True
            if not found_occurrence:
                print(f"No occurrences of the word '{search_term}' found in {file_to_search}")
    except FileNotFoundError as file_error:
        print(f"Error: {file_error}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error! Please enter the search term along with the file name.")
        sys.exit(1)

    search_term_input = sys.argv[1]
    file_name_to_search = sys.argv[2]
    grep_search(search_term_input, file_name_to_search)
