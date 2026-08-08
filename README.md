# MetaTrader 5 Container

MetaTrader 5 Container is an unofficial, pre-built MT5 container using Wine. 

All packages are created by installing MetaTrader 5 from the official installer, then built and packaged in GitHub Actions to ensure a safe, malware-free build.

Delivery with 2 format:
1. Docker image [ghcr.io/thodinh/mt5](https://github.com/thodinh/metatrader5-portable/releases/latest/download/metatrader5.tar.gz).
2. Portable package [metatrader5.tar.gz](https://github.com/thodinh/metatrader5-portable/releases/latest/download/metatrader5.tar.gz), can use both for Window and Linux (Wine 10+).

Verify the SHA256 checksum provided in the release notes to confirm the integrity of your downloaded package.

## Official Resources

- [MetaTrader 5](https://www.metatrader5.com/)
- [MetaTrader 5 Downloads](https://www.metatrader5.com/en/download)

I don't work for MetaQuotes. This is a community effort.

## Download

| Package                                   | Size    | Link                                                                                                              |
| ----------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| **Full** (terminal + editor + tester)     | \~174MB | [metatrader5.tar.gz](https://github.com/thodinh/metatrader5-portable/releases/latest/download/metatrader5.tar.gz) |
| **MetaEditor** (editor + MQL5 + Profiles) | \~47MB  | [metaeditor.tar.gz](https://github.com/thodinh/metatrader5-portable/releases/latest/download/metaeditor.tar.gz)   |

> SHA256 checksums are in the [release notes](https://github.com/thodinh/metatrader5-portable/releases/latest).

## Usage

### With Wine (Linux)

Requires Wine >= 5.x with `winecfg -v=win11`.

```bash
# Download and extract
curl -LO https://github.com/thodinh/metatrader5-portable/releases/latest/download/metatrader5.tar.gz
tar -xzf metatrader5.tar.gz
```

### Docker

Image available on GHCR: `ghcr.io/thodinh/mt5` - runtime with Wine 10+, MT5 pre-installed at `/opt/mt5`

```bash
docker pull ghcr.io/thodinh/mt5:latest
```
Build your own Docker image from the base image:

```dockerfile
FROM ghcr.io/thodinh/mt5:latest

COPY my-ea.ex5 /opt/mt5/MQL5/Experts/
CMD ["wine", "/opt/mt5/terminal64.exe"]
```

### macOS / Apple Silicon

The image is x86_64 only. On Apple Silicon (M1/M2/M3/M4), Docker Desktop does not support x86 emulation properly. Use **Colima** instead:

```bash
brew install colima
colima start
```

Then run with explicit platform:

```bash
docker run --platform linux/amd64 ghcr.io/thodinh/mt5:latest ...
```

### Directory Structure

```
Metatrader-5/
├── terminal64.exe      # MT5 Client Terminal
├── MetaEditor64.exe    # MetaEditor IDE
├── metatester64.exe    # Strategy Tester
├── MQL5/               # Include & Scripts (.ex5 removed)
├── Profiles/           # Chart profiles & templates
└── Config/
    ├── terminal.ini    # LiveUpdate disabled
    └── common.ini      # Experts enabled
```
