# 🔍 Async TLS Port Scanner

A fast **asynchronous Python 3.10 port scanner** that checks open ports across multiple IPs and determines supported **TLS versions**.  
Results are exported to an **Excel file** for easy reporting.

---

## ✨ Features

- 🚀 **Asynchronous scanning** using `asyncio` for high performance
- 🌍 Reads target IPs from `ip.txt`
- 🔒 Detects supported **TLS versions** (`SSLv2`, `SSLv3`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`)
- 📊 Saves results in an **Excel report** (`scan_results.xlsx`)
- ⚡ Configurable concurrency limit to avoid `Too many open files` errors
- 🛡 Works on Linux & macOS (tested with Python **3.10+**)

---

## 📂 Project Structure

├── port-scanner.py # Main script
├── ip.txt # List of target IPs (one per line)
├── scan_results.xlsx # Generated Excel report (after scan)
└── README.md # This file


---

## 📦 Requirements

Install dependencies with:

```bash
pip install openpyxl


(Optional but recommended for TLS testing):

pip install cryptography
```

##  ⚙️ Usage
Add your target IPs to ip.txt (one per line):

```bash
192.168.1.0/24
192.168.5.0/27
```
## ⚡ Performance Notes
Default concurrency is 500 simultaneous connections (MAX_CONCURRENT in script).
If you see Too many open files:
Increase system limits:

```bash
ulimit -n 65535

```
Or reduce concurrency inside the script.

## 📊 Example Output
IP          	Port	Status	TLS Versions Supported <br>
192.168.88.1	443	    OPEN	TLSv1.2, TLSv1.3 <br>
192.168.88.2	443	    CLOSED	— <br>
192.168.88.3	8443	OPEN	TLSv1.0, TLSv1.1, TLSv1.2 <br>

## ⚖️ Disclaimer
This tool is intended for security testing and auditing on networks you own or have explicit permission to scan.
Unauthorized scanning may be illegal in your jurisdiction.