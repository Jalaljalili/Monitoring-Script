# Log Search Script

This script searches for a specific word in a log file and counts the number of occurrences of that word.
# Requirements

    Python 3.x

# Usage

    Save the script to a file, for example log_search.py.
    Replace "/path/to/logfile.log" with the actual path to your log file, and "error" with the word you want to search for.
    Open a terminal and navigate to the directory where the script is saved.
    Run the script by typing python log_search.py in your terminal.
    The script will output the number of occurrences of the search term in the log file.

# Example

If you want to search for the word "error" in the log file /var/log/syslog, you would replace log_file_path = "/path/to/logfile.log" with log_file_path = "/var/log/syslog", and search_term = "error" would be already set.
# License

This script is released under the MIT License. Feel free to use, modify, and distribute it as you wish.


# Size_file
Finding file by Size

```bash
 find / -type f -size +700M -exec ls -lh {} \; 2> /dev/null | awk '{ print $NF ": " $5 }' | sort -nk 2,2
 ```
