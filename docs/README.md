# Lindamood Truck Ticket Sorter 🧾

A GUI-based OCR utility that classifies scanned truck ticket pages by vendor, extracts ticket numbers, and outputs sorted PDFs or TIFFs with Excel logs.

## Features

- Multi-engine OCR (PaddleOCR by default)
- PDF, TIFF, and image input support
- Vendor matching via keywords with optional template fallback
- Grouped exports per vendor
- Logging of ticket numbers and OCR text

## Installation

1. Clone the repository and install requirements:
   ```bash
   git clone https://github.com/your-org/ticket-sorter.git
   cd ticket-sorter
   pip install -r requirements.txt
   ```
2. Download Poppler and set the `POPPLER_PATH` environment variable or update `poppler_path` in `configs.yaml`.
3. On first run the PaddleOCR model files will be downloaded automatically.

## Usage

Launch the GUI:
```bash
python gui.py
```

Select files or a folder and press **Run Sorter**. Results are written to the output directory configured in `configs.yaml`.

## Configuration

`configs.yaml` controls output format, preprocessing options, and template matching settings. Vendor keywords live in `ocr_keywords.xlsx`.

## Developer Notes

OCR logic resides in `processor/hybrid_ocr.py` while image extraction and template matching live in `processor/image_ops.py`.

## Requirements

- Python 3.9+
- paddleocr
- pytesseract
- pdf2image
- opencv-python
- and other packages listed in `requirements.txt`

