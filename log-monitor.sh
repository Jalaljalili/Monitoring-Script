#!/bin/bash

LOG_DIR="/root/log"

# Loop through all log files in the directory
for LOG_FILE in $LOG_DIR/*.log; do
    # Extract the service name from the log file name
    SERVICE_NAME=$(basename "$LOG_FILE" .log).service

    # Count the occurrences of "Invalid data" in the log file
    ERROR_COUNT=$(grep -c "Invalid data" "$LOG_FILE")

    # Check if the error count exceeds the threshold
    if [ "$ERROR_COUNT" -gt 20 ]; then
        echo "Restarting service: $SERVICE_NAME"
        systemctl restart "$SERVICE_NAME"
    fi
done
