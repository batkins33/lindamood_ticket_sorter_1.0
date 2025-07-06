# Lindamood Ticket Sorter

A desktop utility that uses OCR to classify and rename scanned truck tickets. It reads PDF or image files, groups pages by vendor and exports new PDF/TIFF files along with Excel logs.

See the [full guide](docs/README.md) for detailed instructions and configuration.

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
