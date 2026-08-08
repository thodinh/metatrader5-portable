#!/bin/bash

# Default image
IMAGE="ghcr.io/thodinh/mt5:latest"

# Get absolute path of the current directory (assuming script is run from project root)
WORKSPACE_DIR=$(pwd)

# Apple Silicon detection
if [[ "$(uname -m)" == "arm64" ]] || [[ "$(uname -m)" == "aarch64" ]]; then
    echo "=============================================="
    echo "[WARNING] Apple Silicon (ARM64) detected!"
    echo "The MT5 Docker image is x86_64 only."
    echo "Emulation will be slow and may be unstable."
    echo "=============================================="
    echo ""
    if ! command -v colima &>/dev/null; then
        echo "[ERROR] Colima is required on macOS. Install it first:"
        echo "  brew install colima"
        exit 1
    fi
    if ! colima status &>/dev/null; then
        echo "[ERROR] Colima is not running. Start it with:"
        echo "  colima start"
        exit 1
    fi
    echo "Colima is running. Proceeding with amd64 emulation..."
    echo ""
fi

echo "Pulling latest image: $IMAGE..."
docker pull $IMAGE

echo "Running tests in Docker container..."
docker run --platform linux/amd64 -v "$WORKSPACE_DIR:/root/workspace/mt5" --rm $IMAGE bash /root/workspace/mt5/example/run_all.sh

echo "Done!"
