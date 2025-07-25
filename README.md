# IOC Scanner Project 🐍🔍

**Contributors:** Max Z, Michal T, Uzair A

---

## 🚀 Project Overview

The IOC Scanner Project is a Python-based tool designed to scan directories for files that match known Indicators of Compromise (IOCs) based on SHA256 hashes. This helps security analysts and researchers quickly identify potentially malicious files within large data sets or file systems.

---

## 🔍 What It Does

- Loads IOC hashes from a CSV file.
- Recursively scans a specified folder.
- Calculates SHA256 hashes of each file efficiently using memory-friendly chunking.
- Compares file hashes against known IOC hashes.
- Generates detailed reports in TXT or CSV formats listing matched files.

---

## 📁 Project Structure

```
ioc-scanner-project/
├── ioc_scanner/
│ ├── init.py # Package marker
│ ├── ioc_loader.py # Load IOC hashes from CSV
│ ├── hash_utils.py # SHA256 hashing utilities
│ ├── scanner.py # Folder scanning and matching logic
│ ├── report.py # Report generation in TXT/CSV
│
├── tests/
│ ├── test_ioc_loader.py # Unit tests for IOC loader
│ ├── test_hash_utils.py # Tests for SHA256 hashing
│ ├── test_scanner.py # Tests scanning logic
│ ├── test_report.py # Tests report creation
│
├── sample_files/
│ ├── benign.txt # Safe example file
│ ├── infected_sample.exe # File matching IOC hash for testing
│
├── meeting_notes/ # Project discussions and notes
│
├── main.py # Main entry point script
├── requirements.txt # Python dependencies
├── sample_iocs.csv # Sample IOC hashes CSV
├── README.md # This file
├── .gitignore # Files and folders ignored by Git
└── LICENSE # MIT License file
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/zominy/ioc-scanner-project.git
cd ioc-scanner-project

