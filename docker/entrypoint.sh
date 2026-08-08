#!/bin/bash
rm -f /tmp/.X0-lock
rm -f /tmp/.X11-unix/X0 2>/dev/null

echo "Starting Xvfb on :0..."
Xvfb :0 -screen 0 1280x720x24 > /dev/null 2>&1 &
sleep 2

MT5_COMMON="/opt/wineprefix/drive_c/Metatrader-5/Config/common.ini"
if [ -f "$MT5_COMMON" ]; then
    wine python -c "
import sys
data = open('$MT5_COMMON', 'rb').read()
patched = data.replace(b'E\x00n\x00a\x00b\x00l\x00e\x00d\x00=\x000\x00', b'E\x00n\x00a\x00b\x00l\x00e\x00d\x00=\x001\x00', 1)
if patched != data:
    open('$MT5_COMMON', 'wb').write(patched)
"
fi

echo "Applying Read-Only fix to block MT5 LiveUpdate..."
rm -rf /opt/wineprefix/drive_c/users/root/AppData/Roaming/MetaQuotes/WebInstall
mkdir -p /opt/wineprefix/drive_c/users/root/AppData/Roaming/MetaQuotes
touch /opt/wineprefix/drive_c/users/root/AppData/Roaming/MetaQuotes/WebInstall
rm -rf /opt/wineprefix/drive_c/Metatrader-5/WebInstall
touch /opt/wineprefix/drive_c/Metatrader-5/WebInstall

exec "$@"
