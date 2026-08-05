#!/bin/bash
echo "Installing scrot and fluxbox for screenshot debug purpose. This is optional."
apt-get update && apt-get install -y scrot fluxbox

fluxbox &
sleep 2

(
while true; do
    wine /opt/wineprefix/drive_c/Metatrader-5/terminal64.exe /portable
    sleep 2
done
) &

echo "Waiting 15 seconds for MT5 to stabilize..."
sleep 15

for script in /root/workspace/mt5/example/0*.py; do
    echo "=========================================="
    echo "Running $script"
    wine python "$script"
    echo "=========================================="
done

echo "=========================================="
echo "Running 05_screenshot.sh"
bash /root/workspace/mt5/example/05_screenshot.sh
echo "=========================================="
