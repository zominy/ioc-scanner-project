# Max Zominy   04/09/2025   Version 1.1

# scanner.py: Walk through a folder, hash each file, and check against IOC hashes.

import os
from typing import List, Tuple, Set

# ---------------------
# IMPORT HASH FUNCTION
# ---------------------
# Instead of a placeholder fake hash function, I have now imported Michal’s draft
# hash function from hash_utils.py. 
# NOTE: Michal’s version has some issues (e.g. "while true" should be "while True",
# and it does not return the digest). But I am keeping it integrated anyway
# to show that the main project pipeline is complete.
from ioc_scanner.hash_utils import filehash

# ----------------
# SCANNER FUNCTION
# ----------------
def scan_folder_for_hashes(folder_path: str, ioc_hashes: Set[str]) -> List[Tuple[str, str]]:
    """
    Walk through a folder, hash each file, and check if the hash matches an IOC.

    Args:
        folder_path (str): The path to the folder to scan.
        ioc_hashes (Set[str]): A set of known bad SHA256 hashes (IOCs).

    Returns:
        List[Tuple[str, str]]: A list of tuples containing (file_path, matching_hash).
    """

    matches = []  # Stores (file_path, matching_hash) pairs

    # Walk the folder recursively
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            try:
                # Call Michal’s hashing function.
                # NOTE: Currently, filehash() will not work correctly until fixed.
                file_hash = filehash(file_path)

                # Normalise hash formatting (in case of uppercase or extra spaces).
                normalised_hash = file_hash.lower().strip()

                # Check if this hash is in the IOC set.
                if normalised_hash in ioc_hashes:
                    matches.append((file_path, normalised_hash))

            except Exception as e:
                # Catch and report errors (e.g., permission denied, broken files).
                print(f"[!] Error scanning {file_path}: {e}")

    return matches


# --------------------
# MAIN EXECUTION BLOCK
# --------------------
if __name__ == "__main__":
    # Example IOC set for testing (replace with real IOCs later).
    sample_iocs = {
        "deadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"
    }

    folder_to_scan = "sample_files"

    results = scan_folder_for_hashes(folder_to_scan, sample_iocs)

    if results:
        print("[+] Matches found:")
        for file_path, file_hash in results:
            print(f" - {file_path} | {file_hash}")
    else:
        print("[-] No matches found.")