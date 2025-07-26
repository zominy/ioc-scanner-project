# (Notes from Max) This file defines the logic for calculating a file’s SHA256 hash.

# What the Function Does:
# Define a function (e.g., hash_file) that accepts a file path.

# Inside the function:

# Open the file in binary mode ('rb'), not text mode, because hashes are based on raw bytes.

# Read the file in chunks (e.g., 4KB at a time) to avoid memory problems with large files.

# Update the hash object with each chunk of data.

# After reading the full file, return the final SHA256 hash string (in hexadecimal).

# Handle any exceptions (like if the file can’t be opened).

# Why:
# SHA256 is the standard for file integrity checking and matching hashes.

# Reading in chunks makes it memory efficient.