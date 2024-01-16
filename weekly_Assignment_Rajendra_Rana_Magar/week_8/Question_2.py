import sys


def compare_files(file_path1, file_path2):
    try:
        with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
            content_file1 = file1.read()
            content_file2 = file2.read()

            if content_file1 == content_file2:
                print(f"The contents of '{file_path1}' and '{file_path2}' are identical.")
            else:
                print(f"The contents of '{file_path1}' and '{file_path2}' differ.")
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error! Please enter two file names to compare.")
        sys.exit(1)

    file_path_1st = sys.argv[1]
    file_path_2nd = sys.argv[2]
    compare_files(file_path_1st, file_path_2nd)
