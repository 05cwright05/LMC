from pathlib import Path
from PIL import Image
import sys
import pytesseract
import re

def ExtractText(path):
    #use regex to extract the name of the video and the name of the photo within the video
    match = re.search(r'^.+?/([^/]+)/([^/]+)\.', path)
    if match:
        folder_name, file_name = match.groups()
        # Construct the full path
        full_path = f"extracted_text/{folder_name}/{file_name}.txt"
        # Create the folder extracted_text/funny_name
        Path(f"extracted_text/{folder_name}").mkdir(parents=True, exist_ok=True)

    else:
        print("Invalid path format")
        exit
    f = open(full_path, "w")
    f.write(pytesseract.image_to_string(Image.open(path)))
    f.close()

# Driver Code 
if __name__ == '__main__': 
    if len(sys.argv) < 2:
            print("You need to specify a file to be processed")
            sys.exit(1)
    ExtractText(sys.argv[1])
