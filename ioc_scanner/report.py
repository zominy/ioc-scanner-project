# (Notes from Max) This file takes the list of matched files and their hashes and writes them to a .txt or .csv file.

# What the Function Does:
# Define a function (e.g., write_report) that accepts:

# A list of matches (file path + hash).

# The output file path.

# A flag (true/false) that decides if it writes a .csv or .txt.

# Inside the function:

# If writing CSV:

# Open the output file in write mode.

# Write a header row: "File Path", "SHA256".

# Write each file path and hash as one row.

# If writing TXT:

# Open the file in text write mode.

# For each match, write the file path and hash on one line, separated by something like a dash.

# Print a message saying where the file was saved.

# Handle file writing errors with a try-except.

# Why:
# Lets the user choose a format.

# Simple, readable output for both human and machine use.