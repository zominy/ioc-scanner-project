 # Uzair Ali   27/08/2025   Version 1.1
import csv
import os


def load_iocs(path: str) -> set[str]:       #This function takes the file path and returns a set of strings.
    """
    Load SHA256 IOCs from a CSV file into a set.

    Args:
        path (str): Path to the CSV file containing a 'sha256' column.  #These are docstring comments to appear with the help(load_iocs).

    Returns:
        set[str]: A set of normalized SHA256 hashes.
    """
    hashes = set()

    with open(path, newline="", encoding="utf-8") as csvfile:       # This opens the path specific to csv files and uses specific file encoding.
        reader = csv.DictReader(csvfile)  # csv.DictReader reads rows as dictionaries by the colum headers.
        for row in reader:
            #This extracts the value under the sha256 column.
            value = row.get("sha256")       #This grabs the hash directly from the sha256 column.
            if value:
                cleaned = value.strip().lower()  #This removes newlines and makes everything lowercase.
                if cleaned:  #This skips empty rows.
                    hashes.add(cleaned)  #This stores each hash in a set.

    return hashes       #This function gives us back the 'set' with our values.

if __name__ == "__main__":      #Calling the function.
    csv_path = "sample_iocs.csv"   # Make sure this file is in the same directory as your script.
    sha256_set = load_iocs(csv_path)
    print(sha256_set)           #Prints the output.
