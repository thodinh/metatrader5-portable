#!/bin/bash
# This script run in container only, don't try to run

fluxbox &
sleep 5

# Generate login.ini from config.py
cd /root/workspace/mt5/example
wine python -c "
import config
import os
os.makedirs('C:\\\\Metatrader-5\\\\Config', exist_ok=True)
with open('C:\\\\Metatrader-5\\\\Config\\\\login.ini', 'w', encoding='utf-16') as f:
    f.write('[Common]\n')
    f.write(f'Login={config.MT5_LOGIN}\n')
    f.write(f'Password={config.MT5_PASSWORD}\n')
    f.write(f'Server={config.MT5_SERVER}\n')
"

(
while true; do
    wine /opt/wineprefix/drive_c/Metatrader-5/terminal64.exe /portable /config:C:\\Metatrader-5\\Config\\login.ini
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
