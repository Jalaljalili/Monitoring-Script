#!/bin/bash

LOG_FILE=/path/to/logfile.log
SEARCH_TERM="error"

# Check if the log file exists
if [ ! -f "$LOG_FILE" ]; then
    echo "Log file not found: $LOG_FILE"
    exit 1
fi

# Use grep to search for the search term and count the number of matches
NUM_OCCURRENCES=$(grep -c "$SEARCH_TERM" "$LOG_FILE")

# Print the number of occurrences
echo "Number of occurrences of '$SEARCH_TERM' in '$LOG_FILE': $NUM_OCCURRENCES"
