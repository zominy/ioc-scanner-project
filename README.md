# IOC Scanner Project 🐍🔍

**Project Lead and Developer, supported by two Co-Developers:** Max Z (Lead), Michal T, Uzair A

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
├── meetings/ # Project discussions and notes
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
```
2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```
3. Install required packages:

```bash
pip install -r requirements.txt
```

---

## Usage 🛠
Run the scanner via the main script:

```bash
python main.py --ioc-file sample_iocs.csv --scan-folder sample_files/
```
- `--ioc-file`: path to your CSV file with IOC hashes (expects a column named sha256)
- `--scan-folder`: path to folder to scan for matching files

The scanner will generate a report of any matches found.

---

## 🧪 Running Tests

Make sure pytest is installed (add to requirements.txt):

```bash
pip install pytest
```
Run tests with:

```bash
pytest tests/
```

---

## 🤝 Contributing

Contributions are welcome! To collaborate with Max Zominy, Michal T, and Uzair A:

Fork the repository.

Create a feature branch:

```bash
git checkout -b feature/your-feature-name
```
Commit your changes with clear messages:

```bash
git commit -m "Add detailed scanning logic"
```

Push your branch and open a pull request for review.

---

## 📄 License

This project is licensed under the [MIT License](https://mit-license.org/).

---

## 📬 Contact & Support

For questions or support, reach out to the contributors:

Max Zominy: [GitHub](https://github.com/zominy) or [LinkedIn](https://www.linkedin.com/in/max-zominy-85ba92310/)

Michal Twardowski: YET TO ADD

Uzair Ali: YET TO ADD
