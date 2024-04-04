#!/bin/bash

# Check if numpy is installed
echo "Checking if numpy is installed..."
if python -c "import numpy" &> /dev/null; then
    echo "numpy is installed."
else
    echo "Error: numpy is not installed."
    exit 1
fi

# Check if pytest is installed
echo "Checking if pytest is installed..."
if pytest --version &> /dev/null; then
    echo "pytest is installed."
else
    echo "Error: pytest is not installed."
    exit 1
fi

# Check if opencv-python is installed
echo "Checking if opencv-python is installed..."
if python -c "import cv2" &> /dev/null; then
    echo "opencv-python is installed."
else
    echo "Error: opencv-python is not installed."
    exit 1
fi

echo "All required dependencies are installed."

