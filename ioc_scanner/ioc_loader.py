# (Notes from Max) This file reads a .csv file that contains one known malicious SHA256 hash per row and stores those hashes in a set.

# What the Function Does:
# Define a function (e.g., load_iocs) that accepts the path to the IOC file (a .csv).

# Inside the function:

# Open the file using the CSV reader.

# Read each row.

# From each row, extract the value under the column labeled sha256.

# Strip any extra spaces or line breaks from the value.

# Add it to a set.

# Return the set of hashes.

# Why:
# Using a set makes it fast to compare later (O(1) lookup time).

# Handles CSVs properly, so it works with real-world IOC files.