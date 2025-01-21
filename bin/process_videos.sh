#!/bin/bash
echo "Processing all files in 'videos' folder"
for filename in videos/*; do
    echo "Processing: $filename"
    python3 capture_frames.py "$filename"
done
echo "ALL FILES PROCESSED"