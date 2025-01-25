# LMC - On Screen Description Program

The goal of this repository is to produce short, keyword rich descriptions of what a user is experiencing on screen. 

This is accomplished by splitting a video into images every TR (1.5 seconds), extracting the text from these images, and analyzing that text to produce a concise description of the onscreen content.
<br></br>


## Setup

1. Ensure you are using either a UNIX based operating system or are running WSL 

2. cd `/LMC/`

3. Run `bin/setup.sh`

4. Run `source venv/bin/activate` each time you relaunch the repository to ensure that you are in the correct environment

<br></br>

## Quick Start Guide

Follow these steps to fully process your videos and produce CSV files of their content descriptions:

1. Place each video for analysis into `videos/`

2. Ensure you have followed the [Setup](#setup) guide and have activated the virtual environment

3. Run `bin/analyze.sh`

4. Your final results will be in a generated folder called: `results/$VIDEO_NAME_descriptions.csv/`

<br></br>

## Author

- **Caden Scott Wright** 

    - GitHub: [05cwright05](https://github.com/05cwright05)  
    - Email: cadenscottwright@gmail.com
