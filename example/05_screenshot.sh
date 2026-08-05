#!/bin/bash

echo "Preparing to take a screenshot..."
sleep 2

OUTPUT_PATH="/root/workspace/mt5/example/screenshot_example.png"
DISPLAY=:0 scrot "$OUTPUT_PATH"

if [ $? -eq 0 ]; then
    echo "Screenshot successfully saved to: $OUTPUT_PATH"
else
    echo "Failed to take screenshot. Please ensure 'scrot' is installed and DISPLAY is correctly set."
fi
