#!/bin/bash

# Platform detection (macOS/Linux)
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Running on macOS"
    cd frontend || exit
    npm install
    npm run dev

elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Running on Linux"
    cd frontend || exit
    npm install
    npm run dev
else
    echo "Unsupported OS. This script only supports macOS or Linux."
    exit 1
fi
