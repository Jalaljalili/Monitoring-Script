# URL & Port Scanner
This script checks whether a list of URLs are up or down and scans all 65,535 ports for open ones. The results are saved in an Excel file.

## Requirements
Ensure you have Python installed (>=3.6) and install the required dependencies:
``` shell
pip install requests xlsxwriter
```
## Usage
1. Create a 'urls.txt' file and add one URL per line.

2. Run the script:

```shell
python script.py
```

3. The results will be saved in scan_results.xlsx with columns:

    * URL: The checked URL

    * Status: "UP" if reachable, "DOWN" otherwise

    * Open Ports: List of open ports or "None"

## How It Works

* The script reads URLs from urls.txt.

* It checks if each URL is accessible.

* If accessible, it scans all 65,535 ports using multithreading.

* The results are exported to an Excel file.

## Notes

* Port scanning can take time, depending on the number of URLs and open ports.

* Running this script against external servers may require permission.

# TLS Check Version
