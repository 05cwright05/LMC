from pathlib import Path
from PIL import Image
import sys
import pytesseract

def ExtractText(path):
    path_body = "/".join(path.split("/")[1:3])
    full_path =  "extracted_text/" + path_body.split(".")[0] + "_text.txt"
    #create the folder extracted text / video name
    Path(f"extracted_text/{path.split('/')[1]}").mkdir(parents=True, exist_ok=True)
    f = open(full_path, "w")
    f.write(pytesseract.image_to_string(Image.open(path)))
    f.close()

# Driver Code 
if __name__ == '__main__': 
    print(sys.argv)
    if len(sys.argv) < 2:
            print("You need to specify a file to be processed")
            sys.exit(1)
    ExtractText(sys.argv[1])
