import cv2 
import sys
from pathlib import Path

# Function to extract frames 
def FrameCapture(path): 

    # Path to video file 
    vidObj = cv2.VideoCapture(path) 

    # Check if the video file opened successfully
    if not vidObj.isOpened():
        print(f"Error: Could not open video file {path}")
        return

    # track num frames
    num_frames = 0

    #create a folder name for this video
    path_header = "processed/" + path.split("\\")[1].split(".")[0]

    #generate that folder
    Path(path_header).mkdir(parents=True, exist_ok=True)

    # checks whether frames were extracted 
    success = 1

    while True: 
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 

        if not success:  # Break when no more frames
            break

        # Saves the frames with frame-count 
        cv2.imwrite(f"{path_header}/frame{num_frames}.jpg", image) 

        num_frames += 1
    
    print(num_frames)


# Driver Code 
if __name__ == '__main__': 
    if len(sys.argv) < 2:
            print("You need to specify a file to be processed")
            sys.exit(1)
    print(sys.argv[1])
    FrameCapture(sys.argv[1])
