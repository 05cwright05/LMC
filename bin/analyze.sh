#!/bin/bash
echo "Running full process, make sure the videos you want to process are in the videos folder"
bin/setup.sh
bin/process_videos.sh
bin/extract_text.sh

