# Lindamood Truck Ticket Sorter 🧾

A GUI-based OCR tool that classifies scanned truck ticket pages by vendor, extracts ticket numbers, and outputs sorted PDFs or TIFFs with Excel logs.

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
   You can optionally install the project in editable mode so the
   `lindamood-sorter` command is available:
   ```bash
   pip install -e .
   ```
2. Download Poppler and set the `POPPLER_PATH` environment variable or update
   `poppler_path` in `configs.yaml`. Windows users can grab a prebuilt archive
   from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases)
   and point the configuration to the extracted `bin` folder. On macOS simply
   run `brew install poppler`.
3. Install Tesseract if you plan to use the tesseract OCR engine. Ensure the
   `tesseract` executable is available in your `PATH` or set
   `pytesseract.pytesseract.tesseract_cmd` accordingly. Windows builds can be
   found on the [UB Mannheim site](https://github.com/UB-Mannheim/tesseract/wiki)
   while macOS users may install with `brew install tesseract`.
4. On first run the PaddleOCR model files will be downloaded automatically.

## Usage

### Running the GUI

```bash
python gui.py
```

Select files or a folder and press **Run Sorter**. Results are written to the output directory configured in `configs.yaml`.

### Running from the Command Line

```bash
python -m main --file "path/to/your/input.pdf"
```

### Running from PyCharm

1. Open `gui.py` in PyCharm.
2. Ensure your interpreter is set correctly.
3. Run the file using the green ▶️ button.

## Processing Workflow

1. **Extraction** – pages are extracted from PDFs or image files using `pdf2image`.
2. **OCR** – each page is optionally rotated or converted to grayscale before text is read by the configured OCR engine.
3. **Vendor Matching** – the OCR text is compared to keywords from `ocr_keywords.xlsx`. If no match is found, template images in `template_dir` can be used as a fallback.
4. **Export** – pages are grouped by vendor and exported as either PDF or TIFF. A combined PDF can also be created.
5. **Logging** – Excel logs record page numbers, vendor names and ticket numbers. Additional OCR text logs and overlay PDFs are saved in the log directory.

## Configuration Reference (`configs.yaml`)

| Option | Description |
|--------|-------------|
| `cache_file` | Optional path used to store OCR cache data. |
| `exclude_keywords` | List of terms ignored during vendor keyword matching. |
| `keyword_file` | Excel file containing vendor keywords and types. |
| `log_dir` | Directory where Excel logs are written. |
| `ocr_back_pages` | When `true`, OCR is also run on back pages in two-page scans. |
| `ocr_crop_top_percent` | Percent of page height to OCR when ROI cropping is enabled. |
| `ocr_engine` | OCR engine to use (`paddleocr` or `tesseract`). |
| `output_dir` | Destination directory for processed files. |
| `output_format` | Either `pdf` or `tif` for vendor exports. |
| `pdf_resize_scale` | Scale factor applied when creating combined PDFs. |
| `pdf_resolution` | DPI used for combined PDF pages. |
| `poppler_path` | Path to Poppler binaries required for PDF conversion. |
| `preprocess.grayscale` | Convert pages to grayscale before OCR. |
| `preprocess.rotate` | Attempt to auto-rotate pages before OCR. |
| `rename_original` | Move the original file to an archive folder after processing. |
| `source_path` | Default file or folder processed when launching the GUI. |
| `template_dir` | Directory containing vendor template images. |
| `template_threshold` | Confidence threshold for template matching. |
| `two_page_scan` | Treat alternating pages as front/back pairs. |
| `use_roi` | Limit OCR to the top portion of each page. |
| `use_template_fallback` | Try template matching when keyword OCR fails. |

## Folder Structure

- `main.py` – CLI entry point
- `gui.py` – GUI interface
- `processor/` – Processing logic and OCR
- `utils/` – Loader, configuration helpers and keywords
- `template_dir/` – Image templates for fallback matching

## Developer Notes

OCR logic resides in `processor/hybrid_ocr.py` while image extraction and template matching live in `processor/image_ops.py`.

## Requirements

- Python 3.9+
- paddleocr
- pytesseract
- pdf2image
- opencv-python
- Poppler (for PDF conversion)
- Tesseract OCR if using the tesseract engine
- and other packages listed in `requirements.txt`
