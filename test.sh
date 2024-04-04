#!/bin/bash

# Check if Python 3 is installed
echo "Checking if Python 3 is installed..."
if command -v python3 &> /dev/null; then
    echo "Python 3 is installed."
else
    echo "Error: Python 3 is not installed."
    exit 1
fi

echo "All required dependencies are installed."

