FROM docker.io/tobix/pywine:3.9 AS builder

WORKDIR /tmp

ENV WINEPREFIX=/opt/wineprefix
ENV DRIVE_C=${WINEPREFIX}/drive_c
ENV MT5_DIR=${DRIVE_C}/Metatrader-5

ENV URL="https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe" \
    URL_WEBVIEW="https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/c1336fd6-a2eb-4669-9b03-949fc70ace0e/MicrosoftEdgeWebview2Setup.exe"

RUN apt-get update && apt-get install -y --no-install-recommends wget \
    && wget -q $URL && wget -q $URL_WEBVIEW \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN printf 'winecfg -v=win11\nwine MicrosoftEdgeWebview2Setup.exe /silent /install\nwineserver -w\nwine mt5setup.exe /auto /path:"C:\\\\Metatrader-5"\nwineserver -w\n' > /tmp/install-mt5.sh \
    && chmod +x /tmp/install-mt5.sh \
    && xvfb-run /tmp/install-mt5.sh \
    && rm /tmp/install-mt5.sh

RUN printf 'wine "$MT5_DIR/terminal64.exe" /portable &\nfor i in $(seq 1 36); do sleep 10; [ -d "$MT5_DIR/MQL5/Include" ] && break; done\nwineserver -k\n' > /tmp/first-run.sh \
    && chmod +x /tmp/first-run.sh \
    && xvfb-run /tmp/first-run.sh \
    && rm /tmp/first-run.sh

RUN [ -f "$MT5_DIR/terminal64.exe" ] || exit 1

FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive \
    WINEPREFIX=/opt/wineprefix \
    WINEARCH=win64 \
    WINEDLLOVERRIDES="mscoree,mshtml=" \
    WINEDEBUG=-all \
    DISPLAY=:0

ENV DRIVE_C=${WINEPREFIX}/drive_c
ENV MT5_DIR=${DRIVE_C}/Metatrader-5

RUN dpkg --add-architecture i386 && \
    apt-get update && apt-get install -y --no-install-recommends \
    wget gnupg2 software-properties-common xvfb cabextract apt-transport-https ca-certificates fluxbox scrot && \
    mkdir -pm755 /etc/apt/keyrings && \
    wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key && \
    wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/resolute/winehq-resolute.sources && \
    apt-get update && \
    apt-get install -y --install-recommends winehq-stable && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder ${MT5_DIR} ${MT5_DIR}

RUN mkdir -p ${MT5_DIR}/Config && \
    printf '\377\376' > ${MT5_DIR}/Config/common.ini && printf '[Experts]\r\nEnabled=1\r\n' | iconv -f UTF-8 -t UTF-16LE >> ${MT5_DIR}/Config/common.ini

RUN xvfb-run wine winecfg -v=win11 && \
    wineserver -w && \
    wget -q https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe -O /tmp/python-installer.exe && \
    xvfb-run wine /tmp/python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 && \
    wineserver -w && \
    rm /tmp/python-installer.exe && \
    xvfb-run wine "C:\\Program Files\\Python312\\Scripts\\pip.exe" install --no-cache-dir MetaTrader5==5.0.5640 numpy pandas && \
    wineserver -w

COPY entrypoint.sh /root/entrypoint.sh
RUN chmod +x /root/entrypoint.sh

WORKDIR /root
ENTRYPOINT ["/root/entrypoint.sh"]
