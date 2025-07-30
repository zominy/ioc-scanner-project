# (Notes From Max)

#  Purpose:
# Scan folders for suspicious or unauthorized file extensions, like .exe, .js, .bat, .vbs, .ps1, .dll, etc. Employers love this because it mimics basic threat hunting logic.

# What the Function Does:
# Define a function like filter_suspicious_extensions(folder_path, suspicious_extensions).

# Inside the function:

# Walk the folder recursively (like in scanner.py).

# For each file:

# Get the file extension (os.path.splitext).

# If it matches one in a provided suspicious list:

# Store the file path and extension.

# Return a list of flagged files.

# Why:

# Very easy to understand and extend.

# Fits naturally alongside hash scanning.

# Demonstrates awareness of malware techniques (e.g., rogue scripts dropped in temp folders).

# Lets the user customize the extension list, showing thoughtful design.