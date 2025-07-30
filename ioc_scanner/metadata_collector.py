# Purpose:
# After identifying files with IOC-matching hashes, extract detailed metadata to enrich your report (e.g., timestamps, size, owner). This gives forensic value for investigations.

# What the Function Does:
# Define a function (e.g., collect_file_metadata) that accepts a list of file paths (from matches).

# Inside the function:

# For each file path:

# Get:

# File size (in bytes)

# Creation time

# Last modification time

# File permissions

# (Optional) Owner UID or username

# Format times to human-readable strings.

# Return a list of dictionaries or tuples with:

# File path

# Hash

# Metadata (size, timestamps, etc.)