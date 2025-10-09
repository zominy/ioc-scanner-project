# Michal Twardowski 15/09/2025 version 1.2

import hashlib

# function filehash to accept a file path and return a sha256 hash

def filehash (filepath):

    try:

        # open the file in binary mode 'rb'
        with open(filepath, "rb") as binfile:
            sha256 = hashlib.sha256()

            # read the file in 4KB chunks to avoid RAM issues when dealing with larger files
            while True:
                data = binfile.read(4096)
                if not data:
                    break


                # update the hash object with each chunk of data
                sha256.update(data)

        #after reading the full file, return the final sha256 string
        return sha256.hexdigest()
    
    # handling any exceptions, file path error, input errors
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        raise
    except IOError as e:
        print(f"Error reading file '{filepath}': {e}")
        raise