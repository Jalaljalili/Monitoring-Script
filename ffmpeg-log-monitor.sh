#!/bin/bash

# Define the directory where the logs are located
LOG_DIR="/var/log"

while true
do
  # Loop through all log files with the .log extension in the log directory
  for LOG_FILE in $(find $LOG_DIR -name "*.log")
  do
    # Get the latest line from the log file
    line=$(tail -n 1 $LOG_FILE)

    # Extract the fps value from the line
    fps=$(echo $line | grep -o "fps=[^ ]*" | cut -d= -f2)

    # Check if the fps is less than 22
    if (( $(echo "$fps < 22" | bc -l) ))
    then
      # Get the service name from the log file name
      SERVICE_NAME=$(basename $LOG_FILE .log | sed 's/\(.*\)-.*/\1/').service

      # Restart the service
      systemctl restart $SERVICE_NAME

      # Log the restart
      echo "$(date): $SERVICE_NAME restarted because fps was $fps" >> /var/log/restart.log
    fi
  done

  # Wait for 1 minute before checking again
  sleep 60
done