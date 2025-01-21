#Need to alter this so that it does evert TR instead of every frame 
import cv2 
import sys
from pathlib import Path
import os

# Function to extract frames 
def FrameCapture(path): 

    #define TR as 1.5 seconds
    TR = 1.5

    # Path to video file 
    vidObj = cv2.VideoCapture(path) 

    # Check if the video file opened successfully
    if not vidObj.isOpened():
        print(f"Error: Could not open video file {path}")
        return

    # track num frames
    num_frames = 0
    #track what TR we are on
    current_TR = 0

    #create a folder name for this video
    if os.name == 'nt':  #windows
        path_header = "processed\\" + path.split("\\")[1].split(".")[0]
    else: #linux
        path_header = "processed/" + path.split("/")[1].split(".")[0]

    #generate that folder
    Path(path_header).mkdir(parents=True, exist_ok=True)

    # checks whether frames were extracted 
    success = 1

    #get total number of frames
    total_frames = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get the video frame rate
    fps = vidObj.get(cv2.CAP_PROP_FPS)

    # Calculate the number of frames to skip. the minus 1 is because we are saving one of the frames and skipping everything else
    frames_to_skip = int(TR * fps) - 1

    #get the number of TR
    num_TR = total_frames / (fps * 1.5)

    while success: 
        # Read the next frame to save
        success, image = vidObj.read()

        # Save the current frame
        cv2.imwrite(f"{path_header}/TR{current_TR}_frame{num_frames}.jpg", image)

        # Print status
        print(f"{current_TR} / {num_TR}")

        # Skip frames
        for _ in range(frames_to_skip):
            success = vidObj.grab()  # Grab frames without decoding
            num_frames += 1
            if not success:
                break

        num_frames += 1
        current_TR += 1
    
    print(num_frames)

    print(path + " finished" + "\n" + "---" + "\n")


# Driver Code 
if __name__ == '__main__': 
    if len(sys.argv) < 2:
            print("You need to specify a file to be processed")
            sys.exit(1)
    FrameCapture(sys.argv[1])
