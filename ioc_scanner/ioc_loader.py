# Uzair Ali   23/08/2025   Version 1.0
import csv
import os


def load_iocs(path: str) -> set[str]:       #this function takes the file path and returns a set of strings
    """
    Load SHA256 IOCs from a CSV file into a set.

    Args:
        path (str): Path to the CSV file containing a 'sha256' column.  # these are docstring comments to appear with the help(load_iocs)

    Returns:
        set[str]: A set of normalized SHA256 hashes.
    """
    hashes = set()

    with open(path, newline="", encoding="utf-8") as csvfile:       # this openms the path specific to csv files and uses specific file encoding
        reader = csv.DictReader(csvfile)  # csv.DictReader reads rows as dictionaries by the colum headers
        for row in reader:
            # this extracts the value under the sha256 column
            value = row.get("sha256")       #this grabs the hash directly from the sha256 column
            if value:
                cleaned = value.strip().lower()  # this removes newlines and makes everything lowercase
                if cleaned:  # this skips empty rows
                    hashes.add(cleaned)  # this stores each hash in a set

    return hashes       #this function gives us back the 'set' with our values

if __name__ == "__main__":      #calling the function
    script_dir = os.path.dirname(os.path.abspath(__file__))     #this ensures that you know which folder the script is in, had some trouble with this
    csv_path = os.path.join(script_dir, "sample_iocs.csv")      #this helps locate the path of the csv file

    sha256_set = load_iocs(csv_path)    #this actually calls the function
    print(sha256_set)           #and this displays the function
