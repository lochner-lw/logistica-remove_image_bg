# Logistica – Remove Image Background Tool

**LogisticaRIBT** is a lightweight command‑line utility that turns any image into a PNG with a transparent background.  
It wraps the `rembg` library and runs entirely offline using **ONNX Runtime**.

## Prerequisites
* Linux, macOS, or Windows (WSL)  
* Python 3.8+  
* Git (optional, for cloning)

## Quick start

### 1. Clone & install
```bash
git clone https://github.com/your‑org/logistica.git
cd logistica
./install.sh         # sets up .venv and installs all dependencies
```

### 2. Run
```bash
./run.sh path/to/photo.jpg
# → output.png generated in the same folder
```

You can also run directly:

```bash
source .venv/bin/activate
python main.py path/to/photo.jpg
```

## Output
A file named `output.png` (32‑bit RGBA) is created alongside `main.py`.  
Adjust the name inside `main.py` if you prefer a different output path.

## Manual setup (if you do not use install.sh)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Deactivating the virtual environment
```bash
deactivate
```

## License
This project is released under **CC0 1.0**. See `LICENSE.txt` for details.  
Feel free to use, modify, or redistribute without restriction.

