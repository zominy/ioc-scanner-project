# (Notes from Max) This file walks through the entire folder (and subfolders), hashes every file, and checks if any file hash matches a known bad hash (from the IOCs).

# What the Function Does:
# Define a function (e.g., scan_folder_for_hashes) that takes in:

# The path to the folder.

# The set of known IOC hashes.

# Inside the function:

# Walk through every file in the folder using os.walk().

# This also checks subfolders.

# For each file, get the full path.

# Hash the file using the hashing function from hash_utils.

# Compare the hash with the IOC set.

# If there’s a match, store the file path and the hash together (as a pair).

# Return a list of all matching files (each as a file path and matching hash).

# Why:
# Allows full folder scans.

# Efficient comparison using the hash set.

# Scales to many files and folders.