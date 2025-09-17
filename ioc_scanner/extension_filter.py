# Uzair Ali   17/09/2025   Version 1.0

import os

def filter_suspicious_extensions(folder_path, suspicious_extensions=None): #Defines our function
    """
    Scan a folder recursively for files with suspicious extensions.
    """
    if suspicious_extensions is None:
        suspicious_extensions = ['.exe', '.js', '.bat', '.vbs', '.ps1', '.dll'] #Selects which ecnention types we can select to search for

    suspicious_extensions = [ext.lower() for ext in suspicious_extensions]
    flagged_files = []              #Creates a list of files flagged with the selected extention

    for root, _, files in os.walk(folder_path):         #Goes straight to the root directory to be able to seach through all files on system
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in suspicious_extensions:
                full_path = os.path.join(root, file)
                flagged_files.append((full_path, ext.lower()))

    return flagged_files


if __name__ == "__main__":                          #Creating the main interaction function
    folder_to_scan = input("Enter the folder path to scan: ").strip()       #Insert the directory to search
    
    
    custom_exts = input(                                # Ask user which extensions to look for
        "Enter file extensions to flag (comma-separated, e.g. .exe,.js,.dll), "
        "or press Enter to use defaults: "
    ).strip()

    if custom_exts:
        suspicious_list = [ext.strip() for ext in custom_exts.split(",")]           #Allows the selection of specific extentions
    else:
        suspicious_list = None  # use defaults

    results = filter_suspicious_extensions(folder_to_scan, suspicious_list)

    if results:
        print("\nSuspicious files found:")      #Print of results if found
        for path, ext in results:
            print(f" - {path} ({ext})")
    else:
        print("\nNo suspicious files detected.")            #Print a no results found if nothing is found
