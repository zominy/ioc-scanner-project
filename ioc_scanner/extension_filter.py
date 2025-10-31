# Uzair Ali   17/09/2025   Version 1.2

import os


def filter_suspicious_extensions(folder_path, suspicious_extensions=None):  # Defines our function
    """
    Scan a folder recursively for files with suspicious extensions.
    """
    if suspicious_extensions is None:
        suspicious_extensions = ['.exe', '.js', '.bat', '.vbs', '.ps1', '.dll']  # Selects which extension types we can select to search for

    folder_path = os.path.abspath(folder_path)  # Converts folder path to absolute path (fixes issues when called from main)

    if not os.path.isdir(folder_path):  # Checks if the folder exists before scanning
        raise FileNotFoundError(f"The folder path '{folder_path}' does not exist or is not accessible.")

    suspicious_extensions = [ext.lower() for ext in suspicious_extensions]
    flagged_files = []  # Creates a list of files flagged with the selected extension

    for root, _, files in os.walk(folder_path):  # Goes straight to the root directory to be able to search through all files on system
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in suspicious_extensions:
                full_path = os.path.join(root, file)
                flagged_files.append((full_path, ext.lower()))

    return flagged_files


if __name__ == "__main__":  # Creating the main interaction function
    # Loop until a valid folder path is entered
    while True:
        folder_to_scan = input("Enter The folder(directory) path to scan: ").strip()  # Insert the directory to search
        if not os.path.isdir(folder_to_scan):
            print(f"[!] '{folder_to_scan}' is not a valid folder path. Do not enter file paths. Please try again.\n")  # Invalid folder entered
            continue
        else:
            break  # Valid path provided

    custom_exts = ""  # Initialise variable to avoid linter warnings (prevents red underline)

    # Ask for custom extensions or use defaults
    custom_exts = input(  # Ask user which extensions to look for
        "Enter file extensions to flag (comma-separated, e.g. .exe,.js,.dll), "
        "or press Enter to use defaults: "
    ).strip()

    if custom_exts:
        suspicious_list = [ext.strip() for ext in custom_exts.split(",")]  # Allows the selection of specific extensions
    else:
        suspicious_list = None  # use defaults

    # === Perform scan ===
    try:
        results = filter_suspicious_extensions(folder_to_scan, suspicious_list)
    except FileNotFoundError as e:
        print(f"\n[!] Error: {e}")  # Handle invalid path errors gracefully
        exit(1)

    # === Display results ===
    if results:
        print("\nSuspicious files found:")  # Print results if found
        for path, ext in results:
            print(f" - {path} ({ext})")
    else:
        print("\nNo suspicious files detected.")  # Print a no results found if nothing is found
