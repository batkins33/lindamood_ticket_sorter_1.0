# Lindamood Ticket Sorter

The Lindamood Ticket Sorter is a small OCR tool used to classify and rename scanned truck tickets. It can read PDF or image files, group pages by vendor, and produce new PDF/TIFF files along with Excel logs.

See [`docs/README.md`](docs/README.md) for full documentation.

## Quick start

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set the path to Poppler in `configs.yaml`.
3. Run the GUI:
   ```bash
   python gui.py
   ```

## Running tests

Tests are stored under `tests/`. After installing requirements, run `pytest` to ensure everything works.
