#!/bin/bash

echo "Setting up the development environment, this may take some time"
echo "Verifying OS"
# Ensure the script is running on Linux or WSL
# Check if running on Linux or WSL
if [[ "$(uname -s)" == "Linux" ]]; then
    echo "Running on a Linux System. Proceeding with setup."
else
    echo "This repository is designed to run on Linux or WSL. Please install WSL or switch to a Linux OS before proceeding."
    exit 1
fi
# Check if python3 is installed
echo "Verifying Python Installation"
if ! command -v python3 &> /dev/null; then
    echo "python3 is not installed. Please install it before proceeding."
    exit 1
fi
echo "Python3 already installed"

# Check if venv module is available
echo "Verifying Virtual Environment Package"
if ! python3 -m ensurepip --version &> /dev/null; then
    echo "Error: python3-venv is not installed. Please install it using:"
    echo "sudo apt install python3-venv"
    echo "then rerun setup.sh"
    exit 1
fi
echo "Virtual Environment Package Verified"

echo "Creating Virtual Environment"

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

echo "Environment setup"

# Upgrade pip
echo "Upgrading pip to latest version"
python3 -m pip install --upgrade pip
echo "pip upgraded"

# Install dependencies (if any)
echo "Installing Dependencies"
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi
echo "Dependencies Installed"

echo "Python environment setup complete."