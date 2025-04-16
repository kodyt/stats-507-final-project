#!/bin/bash

# Platform detection (macOS/Linux)
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Running on macOS"
    # Set up and run the backend server on macOS
    cd backend || exit
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    echo "Backend environment set up. Running Flask..."
    python3 app.py

elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Running on Linux"
    # Set up and run the backend server on Linux
    cd backend || exit
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    echo "Backend environment set up. Running Flask..."
    python3 app.py
else
    echo "Unsupported OS. This script only supports macOS or Linux."
    exit 1
fi
