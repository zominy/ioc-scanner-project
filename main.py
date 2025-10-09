# main.py
# IOC Scanner - Main Orchestrator
# Version 1.0 | 09/10/2025
# Written collectively
# Purpose:
# This script brings together all project modules to scan a folder for
# malicious Indicators of Compromise (IOCs). It loads IOC hashes,
# identifies suspicious files, hashes them, compares against known IOCs,
# gathers metadata, and produces a final report.

import os
from ioc_scanner.ioc_loader import load_iocs
from ioc_scanner.extension_filter import filter_suspicious_extensions
from ioc_scanner.scanner import scan_folder_for_hashes
from ioc_scanner.metadata_collector import collect_file_metadata
from ioc_scanner.report import write_report

def main():
    print("=== IOC Scanner ===\n")

    # Step 1 - Load the IOC list (SHA256 hashes) from CSV
    ioc_file = "sample_iocs.csv"
    if not os.path.exists(ioc_file):
        print(f"[!] The IOC file '{ioc_file}' was not found.")
        return
    iocs = load_iocs(ioc_file)
    print(f"[+] Loaded {len(iocs)} IOC hashes.\n")

    # Step 2 - Ask the user which folder to scan
    folder_to_scan = input("Enter the folder path to scan: ").strip()
    if not os.path.isdir(folder_to_scan):
        print(f"[!] '{folder_to_scan}' is not a valid folder path.")
        return

    # Step 3 - Identify suspicious files by extension first
    # (This narrows down what will be scanned for hashes.)
    print("\n[+] Searching for suspicious file extensions...")
    suspicious_files = filter_suspicious_extensions(folder_to_scan)
    print(f"[+] Found {len(suspicious_files)} files with suspicious extensions.\n")

    # Step 4 – Scan the entire folder and compare file hashes to the IOC list
    print("[+] Scanning files for known IOC matches...")
    matches = scan_folder_for_hashes(folder_to_scan, iocs)

    if not matches:
        print("[-] No IOC matches were found.")
        return
    print(f"[+] Found {len(matches)} matching files.\n")

    # Step 5 – Collect metadata about the matched files
    print("[+] Gathering metadata for matched files...")
    metadata = collect_file_metadata(matches)

    # Step 6 – Save the results to a CSV report
    report_path = "ioc_report.csv"
    write_report(matches, report_path, as_csv=True, metadata=metadata)

    print(f"\n[✓] Scan complete. Report saved to '{report_path}'")
    print("=== End of Scan ===")

if __name__ == "__main__":
    main()
