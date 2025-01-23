#!/bin/bash
echo "Processing all files in 'videos' folder"
for directory in processed/*; do
    for filename in $directory/*; do
        echo "Processing: $filename"
        python3 extract_text.py "$filename"
    done
done
echo "ALL FILES PROCESSED"