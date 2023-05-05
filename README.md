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




# Host Info Bash Script

This bash script outputs various information about the host, including memory usage, CPU usage, time zone, host IP, disk size, kernel version, total memory, total CPU, and distribution version.

## Requirements

- Bash

## Usage

1. Save the script to a file, for example `host_info.sh`.
2. Open a terminal and navigate to the directory where the script is saved.
3. Make the script executable by running `chmod +x host_info.sh`.
4. Run the script by typing `./host_info.sh` in your terminal.
5. The script will output a table with the requested information.

## Table Columns

The output table has the following columns:

- Memory Usage: The current memory usage of the system.
- CPU Usage: The current CPU usage of the system.
- Time Zone: The time zone of the system.
- Host IP: The IP address of the host.
- Disk Size: The size of the disk where the root directory is mounted.
- Kernel Version: The version of the Linux kernel.
- Total Memory: The total amount of physical memory installed in the system.
- Total CPU: The total number of CPU cores in the system.
- Distribute Version: The version of the Linux distribution.


+----------------+----------------+----------------+-------------+----------------+----------------+--------------+----------+-------------------+
| Memory Usage   | CPU Usage      | Time Zone      | Host IP     | Disk Size      | Kernel Version | Total Memory | Total CPU| Distribute Version|
+----------------+----------------+----------------+-------------+----------------+----------------+--------------+----------+-------------------+
| 12.3% (1.23 GB)|  5.6%          | America/New_York| 192.168.1.5 | 250.0 GB       | 5.4.0-91-generic| 16.0 GB      | 4        | Ubuntu 20.04.1 LTS|
+----------------+----------------+----------------+-------------+----------------+----------------+--------------+----------+-------------------+

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute it as you wish.


# Size_file
Finding file by Size

```bash
 find / -type f -size +700M -exec ls -lh {} \; 2> /dev/null | awk '{ print $NF ": " $5 }' | sort -nk 2,2
 ```


# Find and Replace Script

This is a shell script that finds a specific word in multiple files and replaces it with another word.

## Usage

1. Open a terminal and navigate to the directory that contains the files you want to search.

2. Run the script using the following command:

```shell
sh find_replace.sh
```

3. Enter the word you want to find when prompted.

4. Enter the word you want to replace it with when prompted.

5. The script will then search for all files that contain the word and replace it with the new word.

6. Once the script is finished, it will output a message to indicate that it is done.

## Notes

- This script only replaces exact matches of the word. If you want to replace partial matches or case-insensitive matches, you will need to modify the `grep` and `sed` commands accordingly.

- Make sure to back up your files before running this script, just in case something goes wrong.

# Ffmpeg Log Monitoring Script

This shell script monitors the logs of multiple FFmpeg services and restarts any service whose FPS falls below a certain threshold. The script extracts the service name from the log file name.

1. The script now defines the directory where the logs are located using the LOG_DIR variable.

2. Inside the loop, the script uses the find command to get a list of all log files with the .log extension in the log directory.

3. The script gets the latest line from the log file as before.

4. The script extracts the fps value from the line as before.

5. If the fps value is less than 22, the script extracts the service name from the log file name using the basename and sed commands. The sed command uses a regular expression to remove the hyphen and anything that comes after it in the log file name.

6. The script restarts the service using the extracted service name.

7. The script logs the restart event to a log file as before.

Note that the regular expression used in the sed command assumes that the log file name follows the pattern servicename.log. If your log file names have a different pattern, you may need to adjust the regular expression accordingly.

The script will run continuously, checking the logs every minute. If the FPS of any service falls below the threshold, the script will restart the service and log the restart event to a file.