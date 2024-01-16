import sys
import shutil


def create_backup(original_file):
    try:
        backup_file = original_file + ".backup"
        shutil.copy2(original_file, backup_file)
        print(f"Backup created: {backup_file}")
    except FileNotFoundError:
        print(f"Error: File '{original_file}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to create a backup of '{original_file}'.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python backup_creator.py <file_name>")
    else:
        file_to_backup = sys.argv[1]
        create_backup(file_to_backup)
