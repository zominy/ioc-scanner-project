# (Notes from Max) This is the script the user runs. It brings everything together.

# What the Script Does:
# At the top of the file:

# Import all four functions: load IOCs, hash files, scan folder, write report.

# Import argparse to read folder path, IOC file path, and report file path from the command line.

# In the main() function:

# Use argparse to get:

# The path to the folder to scan.

# The path to the IOC file.

# The path where to save the report.

# A flag for whether to write .csv or .txt.

# Call the IOC loading function, store the result as a set.

# Call the scanner function with the folder and the IOC set.

# Store the result as a list of matches.

# Call the report function with the matches, report path, and CSV flag.

# Print how many matches were found.

# Why:
# Keeps the logic modular (each part does one thing (especially since we are split up)).

# Easy to change or test each part individually.

# Makes the scanner work with any folder and IOC list.

# Debugging is easier.