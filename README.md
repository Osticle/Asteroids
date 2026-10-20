# Asteroids

A classic Asteroids game built with Python and managed using [uv](https://github.com/astral-sh/uv).

## Prerequisites

- [Git](https://git-scm.com/)
- [uv](https://docs.astral.sh/uv/)

If `uv` is not installed on your system, install it via the official installer:

- macOS and Linux:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- Windows (PowerShell):
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Osticle/Asteroids.git
cd Asteroids
```

### 2. Install dependencies

Create the virtual environment and install the dependencies locked in `uv.lock`:

```bash
uv sync
```

### 3. Run the game

Launch the game entry point using `uv`:

```bash
uv run main.py
```
