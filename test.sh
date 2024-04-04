#!/bin/bash

# Check if Python is installed
echo "Checking if Python is installed..."
if command -v python &> /dev/null; then
    echo "Python is installed."
else
    echo "Error: Python is not installed."
    exit 1
fi

echo "

