# (Notes from Max) This file defines the logic for calculating a file’s SHA256 hash.

import hashlib

# What the Function Does:
# Define a function (e.g., hash_file) that accepts a file path.
def filehash (filepath):
    # Open the fle in binary mode ('rb)
    with open(filepath, "rb") as binfile:
        sha256 = hashlib.sha256()
        # Read the file in chunks to avoid memory problems with large files, this value can be tweaked for optimisation
        while true:
            data = binfile.read(4096)
            if not data:
                break
            # Update the hash object with each chunk of data.
            sha256.update(data)
    # After reading the full file, return the final SHA256 hash string.
    sha256.hexdigest()

# Handle any exceptions (like if the file can’t be opened).

# SHA256 is the standard for file integrity checking and matching hashes.

# Reading in chunks makes it memory efficient.