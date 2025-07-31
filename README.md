# IOC Scanner Project 🐍🔍

**Project Lead and Developer, supported by two Co-Developers:** Max Z (Lead), Michal T, Uzair A.

---

## 🚀 Project Overview

The IOC Scanner Project is a Python-based security tool designed to efficiently scan directories for files matching known Indicators of Compromise (IOCs) via SHA256 hashes. This solution empowers security analysts and researchers to quickly identify potentially malicious files across large datasets or file systems, improving threat detection workflows.

---

## 🔍 What It Does

- Load IOC hashes from standardised CSV files.

- Recursively traverse directories and subdirectories for comprehensive scanning.

- Compute SHA256 hashes for files using memory-efficient chunked reads.

- Compare computed hashes against the IOC set for rapid detection.

- Generate clear, customisable reports in TXT or CSV formats, detailing all matched files.

---

## 📁 Project Structure

```
ioc-scanner-project/
├── ioc_scanner/
│   ├── __init__.py           # Package initialiser
│   ├── ioc_loader.py         # Load IOC hashes from CSV files
│   ├── hash_utils.py         # SHA256 hashing utilities
│   ├── scanner.py            # Directory scanning and IOC matching logic
│   ├── report.py             # Report generation (TXT/CSV)
│   ├── metadata_collector.py # Collects file metadata for analysis
│   ├── extension_filter.py   # Filters files by extension for targeted scanning
│
├── tests/
│   ├── test_ioc_loader.py    # Unit tests for IOC loader
│   ├── test_hash_utils.py    # Unit tests for hashing functions
│   ├── test_scanner.py       # Unit tests for scanning logic
│   ├── test_report.py        # Unit tests for report generation
│
├── sample_files/
│   ├── benign.txt            # Safe example file
│   ├── infected_sample.exe   # Sample file matching IOC hash for testing
│
├── meetings/                 # Project meeting notes and discussions
│
├── main.py                   # Main script to run the scanner end-to-end
├── requirements.txt          # Python dependencies list
├── sample_iocs.csv           # Sample IOC hashes for testing
├── README.md                 # Project documentation and overview
├── .gitignore                # Git ignore rules
└── LICENSE                   # MIT License
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
