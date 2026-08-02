FROM ghcr.io/thodinh/mt5:latest

WORKDIR /app

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir MetaTrader5

COPY check_mt5.py /app/check_mt5.py

CMD ["python", "/app/check_mt5.py"]
