#!/bin/bash

# Get the word to find and replace from user input
echo "Enter the word to find:"
read find_word
echo "Enter the word to replace it with:"
read replace_word

# Find all files in the current directory and its subdirectories that contain the word
files=$(grep -l -r "$find_word" ./*)

# Loop through each file and replace the word with the new word
for file in $files
do
  sed -i "s|$find_word|$replace_word|g" "$file"
done

echo "Done!"
