# MT5 Python CI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a sample Docker image based on `ghcr.io/thodinh/mt5:latest` that installs `MetaTrader5`, includes a Python connectivity check, and wires that check into GitHub Actions.

**Architecture:** Keep the existing MT5 portable build image untouched and add a separate example image under `examples/python-mt5/`. The sample image owns the Python dependency and the connectivity script, while the existing GitHub workflow gains an extra job that builds and runs that sample image. Because the current sandbox has no Docker binary, local end-to-end verification is not possible here, so the workflow becomes the primary runtime verification path.

**Tech Stack:** Docker, Python, GitHub Actions, MetaTrader5 Python package

---

### Task 1: Record the environment limitation

**Files:**
- Modify: `/workspace/docs/superpowers/specs/2026-08-02-mt5-python-ci-design.md`

- [ ] **Step 1: Add the verified sandbox limitation**

```md
- Sandbox hien tai khong co `docker`, vi vay khong the build/run image local trong phien nay.
```

- [ ] **Step 2: No command rerun needed**

Run: `docker version`
Expected: shell reports `command not found: docker`

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/specs/2026-08-02-mt5-python-ci-design.md
git commit -m "docs: record docker limitation in sandbox"
```

### Task 2: Add the Python MT5 sample image

**Files:**
- Create: `/workspace/examples/python-mt5/Dockerfile`
- Create: `/workspace/examples/python-mt5/check_mt5.py`

- [ ] **Step 1: Write the sample Dockerfile**

```dockerfile
FROM ghcr.io/thodinh/mt5:latest

WORKDIR /app

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir MetaTrader5

COPY check_mt5.py /app/check_mt5.py

CMD ["python", "/app/check_mt5.py"]
```

- [ ] **Step 2: Write the Python connectivity check**

```python
import sys

import MetaTrader5 as mt5


TERMINAL_PATH = "/opt/mt5/terminal64.exe"


def main() -> int:
    print(f"MetaTrader5 package version: {getattr(mt5, '__version__', 'unknown')}")
    print(f"Initializing terminal at: {TERMINAL_PATH}")

    if not mt5.initialize(path=TERMINAL_PATH):
        print(f"initialize() failed: {mt5.last_error()}", file=sys.stderr)
        return 1

    version = mt5.version()
    print(f"Connected to terminal, version={version}")
    mt5.shutdown()
    print("shutdown() completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: Local build command for environments that have Docker**

Run: `docker build -t mt5-python-smoke:local /workspace/examples/python-mt5`
Expected: image builds successfully

- [ ] **Step 4: Local run command for environments that have Docker**

Run: `docker run --rm mt5-python-smoke:local`
Expected: script prints package version, terminal version tuple, and exits `0`

- [ ] **Step 5: Commit**

```bash
git add examples/python-mt5/Dockerfile examples/python-mt5/check_mt5.py
git commit -m "feat: add mt5 python sample image"
```

### Task 3: Add CI coverage for the sample image

**Files:**
- Modify: `/workspace/.github/workflows/build-mt5.yml`

- [ ] **Step 1: Add a separate smoke-test job**

```yaml
  python-mt5-smoke:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Python MT5 sample image
        run: docker build -t mt5-python-smoke:ci examples/python-mt5

      - name: Run Python MT5 smoke test
        run: docker run --rm mt5-python-smoke:ci
```

- [ ] **Step 2: Keep the existing release-oriented build job unchanged**

```yaml
jobs:
  build:
    ...
  python-mt5-smoke:
    ...
```

- [ ] **Step 3: Validate workflow syntax**

Run: `python - <<'PY'\nimport yaml, pathlib\nprint(yaml.safe_load(pathlib.Path('/workspace/.github/workflows/build-mt5.yml').read_text())['jobs'].keys())\nPY`
Expected: prints both `build` and `python-mt5-smoke`

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/build-mt5.yml
git commit -m "ci: add mt5 python smoke test"
```

### Task 4: Final verification

**Files:**
- Review: `/workspace/examples/python-mt5/Dockerfile`
- Review: `/workspace/examples/python-mt5/check_mt5.py`
- Review: `/workspace/.github/workflows/build-mt5.yml`

- [ ] **Step 1: Run diagnostics on changed files**

Run: language diagnostics in the editor for the Python and workflow files
Expected: no newly introduced errors

- [ ] **Step 2: Summarize runtime verification honestly**

```txt
Local Docker verification was not possible in this sandbox because `docker` is unavailable.
GitHub Actions will provide the first real container execution check for this change.
```

- [ ] **Step 3: Commit**

```bash
git add examples/python-mt5/Dockerfile examples/python-mt5/check_mt5.py .github/workflows/build-mt5.yml
git commit -m "chore: finalize mt5 python smoke flow"
```
