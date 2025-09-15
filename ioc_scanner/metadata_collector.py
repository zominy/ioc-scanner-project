# Max Zominy   13/09/2025   Version 1.0
# metadata_collector.py
# Purpose: Collect detailed metadata about files that matched IOCs

import os
import pwd  # Only works on Unix-like systems; optional for Windows, see note
from datetime import datetime
from typing import List, Dict, Tuple

def collect_file_metadata(matched_files: List[Tuple[str, str]]) -> List[Dict[str, str]]:
    """
    Collect metadata for each matched file.

    Args:
        matched_files (List[Tuple[str, str]]): List of tuples (file_path, matching_hash)

    Returns:
        List[Dict[str, str]]: List of dictionaries with file path, hash, and metadata
    """

    metadata_list = []

    for file_path, file_hash in matched_files:
        try:
            # Get basic stats
            stats = os.stat(file_path)

            # File size in bytes
            size = stats.st_size

            # Creation and modification times (formatted)
            created_time = datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
            modified_time = datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")

            # File permissions
            permissions = oct(stats.st_mode)[-3:]  # Simple rwx format

            # Owner username (Unix-only won't work on Windows due to 'pwd' being a Unix command.)
            try:
                owner = pwd.getpwuid(stats.st_uid).pw_name
            except ImportError:
                owner = "N/A (Windows)"
            except KeyError:
                owner = "Unknown"

            metadata_list.append({
                "file_path": file_path,
                "sha256": file_hash,
                "size_bytes": size,
                "created_time": created_time,
                "modified_time": modified_time,
                "permissions": permissions,
                "owner": owner
            })

        except Exception as e:
            # If file cannot be accessed, log with placeholder values
            metadata_list.append({
                "file_path": file_path,
                "sha256": file_hash,
                "size_bytes": "N/A",
                "created_time": "N/A",
                "modified_time": "N/A",
                "permissions": "N/A",
                "owner": "N/A",
                "error": str(e)
            })

    return metadata_list
