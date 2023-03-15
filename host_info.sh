#!/bin/bash

# Get memory usage
MEMORY_USAGE=$(free -h | awk '/^Mem/ {print $3 "/" $2}')

# Get CPU usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 "%" }')

# Get time zone
TIME_ZONE=$(timedatectl | grep "Time zone" | awk '{print $3}')

# Get host IP
HOST_IP=$(hostname -I | awk '{print $1}')

# Get disk size
DISK_SIZE=$(df -h / | awk '/\// {print $2}')

# Get kernel version
KERNEL_VERSION=$(uname -r)

# Get total memory
TOTAL_MEMORY=$(dmidecode -t memory | grep Size | awk '{s+=$2} END {print s "B"}')

# Get total CPU
TOTAL_CPU=$(lscpu | grep "CPU(s)" | head -1 | awk '{print $2}')

# Get distribution version
DISTRIB_VERSION=$(cat /etc/os-release | grep "VERSION_ID" | awk -F '"' '{print $2}')

# Output table
echo "Hostname Info"
echo "--------------------------------------------------"
echo "Memory Usage | CPU Usage | Time Zone | Host IP | Disk Size | Kernel Version | Total Memory | Total CPU | Distribute Version"
echo "--------------------------------------------------"
printf "%-12s | %-9s | %-9s | %-7s | %-9s | %-14s | %-12s | %-9s | %-17s\n" \
       "$MEMORY_USAGE" "$CPU_USAGE" "$TIME_ZONE" "$HOST_IP" "$DISK_SIZE" "$KERNEL_VERSION" "$TOTAL_MEMORY" "$TOTAL_CPU" "$DISTRIB_VERSION"
echo "--------------------------------------------------"
