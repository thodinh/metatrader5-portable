# MT5 Python Container And CI Design

## Muc tieu

Tao mot Dockerfile moi ke thua tu `ghcr.io/thodinh/mt5:latest`, cai package Python `MetaTrader5` bang `pip`, va cung cap mot script Python toi gian de kiem tra kha nang khoi tao ket noi MT5 trong container.

Phan kiem chung uu tien theo thu tu:

1. Kiem tra moi truong sandbox hien tai co du dieu kien de chay thu nhu GitHub Actions hay khong.
2. Neu du dieu kien, build image va chay test local truoc.
3. Chi sau khi test local dat yeu cau moi cap nhat workflow GitHub Actions.

README khong nam trong pham vi thay doi cua dot nay.
Qua kiem tra thuc te trong sandbox hien tai, lenh `docker` khong ton tai, vi vay khong the build/run image local trong phien nay.

## Pham vi thay doi

- Them mot Dockerfile vi du moi, tach biet voi `docker/Dockerfile` dang dung de build va phat hanh MT5 portable.
- Them mot script Python de:
  - import `MetaTrader5`
  - goi `mt5.initialize(path="/opt/mt5/terminal64.exe")`
  - in thong tin loi neu khoi tao that bai
  - goi `mt5.shutdown()` neu khoi tao thanh cong
- Danh gia kha nang build va run Docker trong sandbox hien tai.
- Neu sandbox cho phep, chay build va test local de xac thuc image va script.
- Cap nhat GitHub Actions de lap lai cung buoc build va test nhu da xac thuc local.

## Khong lam trong dot nay

- Khong cap nhat `README.md`.
- Khong cau hinh dang nhap broker bang secrets.
- Khong thay doi quy trinh release image MT5 portable hien co ngoai phan can thiet de them test moi.

## Cau truc de xuat

- `examples/python-mt5/Dockerfile`
  - `FROM ghcr.io/thodinh/mt5:latest`
  - cai `MetaTrader5` bang `python -m pip install --no-cache-dir MetaTrader5`
  - copy script test vao image
  - mac dinh chay script test hoac de CI goi truc tiep
- `examples/python-mt5/check_mt5.py`
  - script test toi gian cho `initialize()` va `shutdown()`
- `.github/workflows/build-mt5.yml`
  - bo sung job hoac step build image vi du
  - chay container de thuc thi script test

## Tieu chi thanh cong

- Docker image vi du build thanh cong tu `ghcr.io/thodinh/mt5:latest`.
- Package `MetaTrader5` duoc cai thanh cong trong image.
- Script Python chay duoc trong container va `mt5.initialize(...)` tra ve thanh cong.
- Neu local sandbox co han che khien khong the build/run Docker, can ghi ro gioi han do va chi cap nhat file o muc hop ly voi ghi chu ve phan chua the xac minh.

## Rui ro va cach xu ly

- `MetaTrader5` co the phu thuoc thu vien he thong hoac cau hinh Wine trong image goc.
  - Cach xu ly: test local truoc khi sua workflow.
- Sandbox co the khong cho phep Docker daemon hoac nested container.
  - Cach xu ly: kiem tra `docker version` va build nho truoc; neu bi chan thi ghi nhan ro va tranh khang dinh da test.
- `mt5.initialize()` co the can chi ro duong dan `terminal64.exe`.
  - Cach xu ly: hardcode duong dan `/opt/mt5/terminal64.exe` trong script.

## Ke hoach thuc hien

1. Kiem tra moi truong hien tai co Docker va kha nang build/run image hay khong.
2. Neu kha dung, tao Dockerfile va script Python.
3. Build image local va chay script test.
4. Neu test local pass, cap nhat GitHub Actions theo cung quy trinh.
5. Chay kiem tra cuoi cho cac file vua sua.
