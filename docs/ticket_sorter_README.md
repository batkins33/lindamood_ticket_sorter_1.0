# Lindamood Ticket Sorter

This application processes scanned truck ticket PDFs using OCR and template matching. It groups pages by vendor,
extracts ticket numbers, and logs the output into Excel.

## ✅ How to Use

### ▶️ Running from PyCharm (GUI Mode)

1. Open `gui.py` in PyCharm.
2. Ensure your interpreter is set correctly.
3. Run `gui.py` directly using the green ▶️ button.

### ⚠️ Note

If you're running scripts like `ocr_utils.py` or `run.py` **directly**, you **must** use module execution to avoid
import errors:

```bash
python -m processor.run
```

---

### ▶️ Running from Command Line (main.py)

This starts the processor with config:

```bash
python -m main --file "path/to/your/input.pdf"
```

Replace `"path/to/your/input.pdf"` with your actual file or folder path.

---

## 🗂 Folder Structure

- `main.py`: CLI entry point
- `gui.py`: GUI interface
- `processor/`: Processing logic and OCR
- `utils/`: Loader, config, keywords
- `template_dir/`: Image templates for fallback matching

