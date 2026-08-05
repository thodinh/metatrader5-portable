#!/bin/bash
(
while true; do
    wine /opt/wineprefix/drive_c/Metatrader-5/terminal64.exe /portable
    sleep 2
done
) &

echo "Waiting 10 seconds for MT5 to stabilize..."
sleep 10

echo "Running connect_test.py..."
wine python /root/connect_test.py
