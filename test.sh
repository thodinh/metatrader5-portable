#!/bin/bash

# Default image
IMAGE="ghcr.io/thodinh/mt5:latest"

# Get absolute path of the current directory (assuming script is run from project root)
WORKSPACE_DIR=$(pwd)

echo "Pulling latest image: $IMAGE..."
docker pull $IMAGE

echo "Running tests in Docker container..."
docker run -v "$WORKSPACE_DIR:/root/workspace/mt5" --rm $IMAGE bash /root/workspace/mt5/example/run_all.sh

echo "Done!"
