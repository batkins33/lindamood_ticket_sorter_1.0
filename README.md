# Lindamood Ticket Sorter

A desktop utility that uses OCR to classify and rename scanned truck tickets. It reads PDF or image files, groups pages by vendor and exports new PDF/TIFF files along with Excel logs.

See the [full guide](docs/README.md) for detailed instructions and configuration.

## Quick start

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   To register the `lindamood-sorter` command you can instead install the
   package in editable mode:
   ```bash
   pip install -e .
   ```
2. Install Poppler and set the path in `configs.yaml` (or the `POPPLER_PATH`
   environment variable). On Windows you can download a prebuilt package from
   [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases);
   macOS users can run `brew install poppler`.
3. Install Tesseract if you plan to use the tesseract OCR engine. Make sure the
   `tesseract` executable is available in your `PATH` or set
   `pytesseract.pytesseract.tesseract_cmd`.
4. Run the GUI:
   ```bash
   python gui.py
   ```

## Running tests

Tests are stored under `tests/`. After installing requirements, run `pytest` to ensure everything works.

## Examples

Example scripts are located in the `examples/` directory. The
`paddle_demo.py` file demonstrates using PaddleOCR separately from the
main application:

```bash
python examples/paddle_demo.py
```

## Module Overview

The project is split into several small modules:

- `main.py` – command line entry point that loads configuration and
  calls the processing pipeline.
- `gui.py` – Tkinter based GUI used for day‑to‑day operation.
- `processor/` – core processing logic with helpers:
  - `run.py` orchestrates batch processing and logging.
  - `hybrid_ocr.py` performs OCR, vendor matching and export.
  - `image_ops.py` handles image extraction and template matching.
  - `file_handler.py` writes Excel logs and grouped output files.
  - `filename_utils.py` parses input file names and builds output names.
- `utils/` – configuration loading, OCR wrappers and timing utilities.
