# Max Zominy   13/09/2025   Version 1.1
# metadata_collector.py
# Purpose: Collect detailed metadata about files that matched IOCs

import os
import platform
import datetime

# Try to import pwd safely (only on Unix)
try:
    import pwd
except ImportError:
    pwd = None  # Windows systems don't have this module, would halt the program before now is excepted.


def collect_file_metadata(file_paths):
    """Collects metadata (size, modified time, owner if available) for matched files."""
    metadata = {}
    for path in file_paths:
        try:
            stats = os.stat(path)
            owner = None
            if pwd:
                # Unix-like: get username
                owner = pwd.getpwuid(stats.st_uid).pw_name
            else:
                # Windows fallback: use environment username
                owner = os.getenv('USERNAME', 'Unknown')

            metadata[path] = {
                'size': stats.st_size,
                'modified': datetime.datetime.fromtimestamp(stats.st_mtime).isoformat(),
                'owner': owner,
                'system': platform.system()
            }
        except Exception as e:
            metadata[path] = {'error': str(e)}
    return metadata

# Reason for update: Would not reliably work on Windows, or MacOS.