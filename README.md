# MetaTrader 5 Portable

MetaTrader 5 Portable is an unofficial, pre-built MT5 portable package using Wine. All packages are created by installing MetaTrader 5 from the official installer, then built and packaged in GitHub Actions to ensure a safe, malware-free build. Always verify the SHA256 checksum provided in the release notes to confirm the integrity of your downloaded package.

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

Image available on GHCR: `ghcr.io/thodinh/metatrader5` - runtime with Wine 10+, MT5 pre-installed at `/opt/mt5`

```bash
docker pull ghcr.io/thodinh/metatrader5:latest
```
Build your own Docker image from the base image:

```dockerfile
FROM ghcr.io/thodinh/metatrader5:latest

COPY my-ea.ex5 /opt/mt5/MQL5/Experts/
CMD ["wine", "/opt/mt5/terminal64.exe"]
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
