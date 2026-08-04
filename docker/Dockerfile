# Stage 1: Build MT5 with proven Wine 5.x/6.x (Debian Bullseye)
FROM docker.io/tobix/pywine:3.9 AS builder

WORKDIR /tmp

ENV HOME=/root \
    DRIVE_C=${WINEPREFIX}/drive_c \
    STOPSIGNAL=SIGRTMIN+3 \
    URL="https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe" \
    URL_WEBVIEW="https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/c1336fd6-a2eb-4669-9b03-949fc70ace0e/MicrosoftEdgeWebview2Setup.exe" \
    MT5_DIR="/opt/wineprefix/drive_c/Metatrader-5"

RUN apt-get update && apt-get install -y --no-install-recommends wget

RUN wget -q $URL && wget -q $URL_WEBVIEW

RUN printf 'winecfg -v=win11\nwine MicrosoftEdgeWebview2Setup.exe /silent /install\nwineserver -w\nwine mt5setup.exe /auto /path:"C:\\\\Metatrader-5"\nwineserver -w\n' > /tmp/install-mt5.sh \
    && chmod +x /tmp/install-mt5.sh \
    && xvfb-run /tmp/install-mt5.sh \
    && rm /tmp/install-mt5.sh

# First run generates MQL5/ (Experts, Include, Indicators...) next to the exe thanks to /portable
RUN printf 'wine "$MT5_DIR/terminal64.exe" /portable &\nfor i in $(seq 1 36); do sleep 10; [ -d "$MT5_DIR/MQL5/Include" ] && break; done\nwineserver -k\n' > /tmp/first-run.sh \
    && chmod +x /tmp/first-run.sh \
    && xvfb-run /tmp/first-run.sh \
    && rm /tmp/first-run.sh \
    && rm -rf "$MT5_DIR/logs" "$MT5_DIR/MQL5/logs" \
    && ls "$MT5_DIR/MQL5"

RUN [ -f "$MT5_DIR/terminal64.exe" ] || exit 1

# Stage 2: Runtime base with Wine 10+ (Debian Trixie)
FROM docker.io/tobix/pywine:3.14

COPY --from=builder /opt/wineprefix/drive_c/Metatrader-5 /opt/mt5

ENV MT5_DIR=/opt/mt5

# Run winecfg once to initialize wineprefix for the target Wine version
RUN wineboot -i 2>/dev/null; winecfg -v=win11 2>/dev/null; wineserver -w

WORKDIR /opt/mt5
