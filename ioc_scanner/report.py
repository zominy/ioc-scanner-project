# Sofiane Laleg   03/10/2025   Version 1.0
import csv
import os
from typing import List, Tuple, Dict, Optional, Any
 
 
def write_report(
    matches: List[Tuple[str, str]],
    output_path: str,
    as_csv: bool = True,
    metadata: Optional[List[Dict[str, Any]]] = None
) -> None:
    """
    Write matched files and their hashes to a report file in CSV or TXT format.
 
    Args:
        matches (List[Tuple[str, str]]): List of (file_path, sha256) tuples.
        output_path (str): Path to save the output report file.
        as_csv (bool): If True, output will be CSV; if False, plain text.
        metadata (Optional[List[Dict[str, Any]]]): Optional detailed metadata
            for each matched file (e.g., size, timestamps).
 
    Returns:
        None
    """
    try:
        # Ensure the output directory exists, create if missing
        dir_name = os.path.dirname(output_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)
 
        if as_csv:
            # Writing output as CSV file
            with open(output_path, mode="w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
 
                if metadata:
                    # Extract extra metadata keys beyond 'file_path' and 'sha256'
                    first_entry = metadata[0]
                    extra_keys = [
                        k for k in first_entry.keys()
                        if k not in ("file_path", "sha256")
                    ]
 
                    # Write CSV header row including metadata fields
                    headers = ["File Path", "SHA256"] + extra_keys
                    writer.writerow(headers)
 
                    # Write each metadata entry as a CSV row
                    for entry in metadata:
                        row = [entry.get("file_path", ""), entry.get("sha256", "")]
                        row.extend(entry.get(k, "") for k in extra_keys)
                        writer.writerow(row)
                else:
                    # No metadata provided; write only file paths and hashes
                    writer.writerow(["File Path", "SHA256"])
                    for file_path, sha in matches:
                        writer.writerow([file_path, sha])
 
        else:
            # Writing output as plain text file
            with open(output_path, mode="w", encoding="utf-8") as txtfile:
                if metadata:
                    # Prepare header line for text file including metadata fields
                    first_entry = metadata[0]
                    extra_keys = [
                        k for k in first_entry.keys()
                        if k not in ("file_path", "sha256")
                    ]
                    header = " | ".join(["File Path", "SHA256"] + extra_keys)
                    txtfile.write(header + "\n")
                    txtfile.write("-" * len(header) + "\n")
 
                    # Write each metadata entry in pipe-separated format
                    for entry in metadata:
                        line_parts = [
                            str(entry.get("file_path", "")),
                            str(entry.get("sha256", ""))
                        ]
                        line_parts.extend(str(entry.get(k, "")) for k in extra_keys)
                        txtfile.write(" | ".join(line_parts) + "\n")
                else:
                    # No metadata: just write file path and hash separated by dash
                    for file_path, sha in matches:
                        txtfile.write(f"{file_path} - {sha}\n")
 
        # Inform user of successful save location
        print(f"[+] Report saved to: {output_path}")
 
    except Exception as e:
        # Catch any exceptions during file operations and report
        print(f"[!] Failed to write report to {output_path}: {e}")
