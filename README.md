# Logistica – Remove Image Background Tool

**LogisticaRIBT** is a lightweight command-line utility that turns any image into a PNG with a transparent background.  
It wraps the `rembg` library and runs entirely offline using **ONNX Runtime**.

Now available as an **npm package** 🚀

---

## 1. Quick start (Node JS users)

```bash
# Install globally
npm i -g logistica-remove-image-bg      # yarn/pnpm works as well

# Use it
logistica-ribt path/to/photo.jpg
# → output.png generated in the same folder
```

The first run builds a local Python virtual-env and downloads the
model weights; subsequent invocations are instantaneous.

---

## 2. Quick start (from source)

```bash
git clone https://github.com/lochner-lw/logistica-remove_image_bg.git
cd logistica-remove_image_bg
npm install          # runs ./install.sh as postinstall
logistica-ribt path/to/photo.jpg
```

---

## 3. Legacy (pure Python)

If you prefer the original workflow:

```bash
./install.sh
source .venv/bin/activate
python main.py path/to/photo.jpg
```

---

## Output
A file named `output.png` (32-bit RGBA) is created alongside `main.py`.  
Adjust the name inside `main.py` if you prefer a different output path.

---

## License
This project is released under **CC0 1.0**. See `LICENSE.txt` for details.  
Feel free to use, modify, or redistribute without restriction.
