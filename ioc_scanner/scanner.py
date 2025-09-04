# Max Zominy   04/09/2025   Version 1.0

# scanner.py: Walk through a folder, hash each file, and check against IOC hashes.

# os: Provides functions to interact with the operating system, such as walking through directories and working with file paths.
# typing: Provides type hints to make the code more explicit and easier to read.
import os
from typing import List, Tuple, Set

# ------------------
# PLACEHOLDER IMPORT
# ------------------
# When Michal finishes hash_utils.py, I will import the real hash function from the file once it is implemented. 
# For now, I am keeping this commented out to show forward planning. 
# from ioc_scanner.hash_utils import hash_file

# --------------------------------
# FAKE HASH FUNCTION (PLACEHOLDER)
# --------------------------------
# This function is here just so that I can test the scanner logic before the real
# hashing code is published. It always returns the same fake hash string.
# In a real implementation, this would open the file, read it in chunks, and
# compute the actual SHA256 hash.
def fake_hash_file(path: str) -> str:
    """
    Temporary placeholder function for hashing files.
    Args:
        path (str): The path of the file to be hashed.
    Returns:
        str: A fake SHA256 hash string (64 hex characters).
    """
    return "deadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef" # Fixed example hash. As previously stated.

# ----------------
# SCANNER FUNCTION
# ----------------
# This is the core function that walks through a folder, calculates (fake)
# hashes for each file, and compares those hashes against a set of known bad
# hashes (IOCs).

def scan_folder_for_hashes(folder_path: str, ioc_hashes: Set[str]) -> List[Tuple[str, str]]:
    """
    Walk through a folder, hash each file, and check if the hash matches an IOC.

    Args:
        folder_path (str): The path to the folder the user wants to scan.
        ioc_hashes (Set[str]): A set of known bad SHA256 hashes (IOCs).

    Returns:
        List[Tuple[str, str]]: A list of tuples containing (file_path, matching_hash).
    """

    # This list will collect results. Each element will be a tuple containing:
    # 1. The path to the suspicious file.
    # 2. The SHA256 hash that matched the IOC list.
    matches = []

    # os.walk() is a generator that allows us to iterate through a directory tree.
    # For each iteration, it gives us:
    # - root: the current folder path
    # - _: a list of subfolders. (Using _ because we do not need it.)
    # - files: a list of file names in the current folder
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            # Building the absolute file path by combining folder path + file name.
            file_path = os.path.join(root, file_name)

            try:
                # Call the placeholder hashing function. Later, this will be replaced
                # with the real hash_file() function that actually computes the hash.
                file_hash = fake_hash_file(file_path)

                # Ensure the hash is normalised (lowercase, no extra spaces).
                # This avoids mismatches due to formatting differences.
                normalised_hash = file_hash.lower().strip()

                # Check if the computed hash is in our set of IOC hashes.
                # Using a set means the lookup is O(1) (very fast, even for thousands of IOCs and pretty easy).
                if normalised_hash in ioc_hashes:
                    # If we have a match, add the tuple (file_path, hash) to the results list.
                    matches.append((file_path, normalised_hash))

            except Exception as e:
                # If something goes wrong (like permission denied, corrupted file, etc.),
                # I do not want the program to crash. Instead, it will print an error and continue.
                print(f"[!] Error scanning {file_path}: {e}")

    # After scanning all files, return the complete list of matches.
    return matches

# --------------------
# MAIN EXECUTION BLOCK
# --------------------
# This section runs only if the script is executed directly (python scanner.py).
# If the file is imported as a module in another script, this part won’t run.
if __name__ == "__main__":
    # Define a small set of IOC hashes for demonstration.
    # Right now, it just contains the fake fixed placeholder hash.
    sample_iocs = {"deadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"}

    # Choose which folder to scan. In this example, it’s the sample_files folder.
    folder_to_scan = "sample_files"

    # Run the scanner with our folder path and IOC set.
    results = scan_folder_for_hashes(folder_to_scan, sample_iocs)

    # If results are found, print them clearly.
    if results:
        print("[+] Matches found:")
        for file_path, file_hash in results:
            # For each match, show the file path and its matching hash.
            print(f" - {file_path} | {file_hash}")
    else:
        # If no matches were found, user is notified.
        print("[-] No matches found.")