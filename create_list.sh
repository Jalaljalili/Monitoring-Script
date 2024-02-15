#!/bin/bash
# Create a list.txt file in the current directory
touch list.txt
# Find all the mp3 files in /PATH/* and append their paths with quotes to list.txt
find /PATH/* -type f -name "*.mp3" | sed "s/^/file '/;s/$/'/" >> list.txt
