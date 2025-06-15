📘 README.md (Developer/Deployment Friendly)
markdown
Copy
Edit

# Lindamood Truck Ticket Sorter 🧾

A GUI-based OCR app that classifies scanned truck ticket pages by vendor, extracts key data, and outputs sorted
PDFs/TIFFs along with structured Excel logs.

## 🚀 Features

- ✅ Multi-engine OCR (PaddleOCR default)
- 📄 PDF, TIFF, JPEG input support
- 🧠 Vendor matching via keywords or fallback template matching
- 🗂️ Grouped exports (per-vendor)
- 📊 Logs with ticket numbers and OCR text
- 🖼️ Template matching fallback (OpenCV)
- 🖥️ GUI front-end with batch support

---

## 🛠️ Installation

1. **Clone the Repo**
   ```bash
   git clone https://github.com/your-org/ticket-sorter.git
   cd ticket-sorter

Install Python dependencies

bash
Copy
Edit
pip install -r requirements.txt
Download and Install Poppler

For PDF image extraction

Add the binary path to configs.yaml under poppler_path

Download PaddleOCR Model Files

Done automatically on first run (ensure internet connection)

📁 Project Structure
graphql
Copy
Edit
ticket-sorter/
│
├── gui.py # Main GUI launcher
├── run.py # Core execution entrypoint
├── configs.yaml # User settings
│
├── processor/
│ ├── hybrid_ocr.py # Page-wise OCR and vendor detection
│ ├── image_ops.py # Image preprocessing, extraction
│ ├── file_handler.py # Output PDF/TIFF logic
│ ├── filename_utils.py # Parsing and naming utilities
│
├── utils/
│ ├── ocr_wrapper.py # OCR abstraction
│ ├── ocr_paddle.py # PaddleOCR engine logic
│ ├── loader.py # Loads templates + keyword configs
│
├── template_dir/ # Directory of per-vendor templates
├── ocr_keywords.xlsx # Match terms (vendor name, type, keywords)
📸 Usage
Launch the GUI:

bash
Copy
Edit
python gui.py
Select file(s) or a folder.

Choose settings like:

PDF or TIFF

Rotation, grayscale, two-page scan

Whether to fallback on template matching

Press Run Sorter!

🔍 OCR Keyword File Format (ocr_keywords.xlsx)
vendor name vendor type ocr match terms
Acme Inc trucking acme, acme corp
GravelCo materials gravelco, gvl, gravel

⚙️ Config File (configs.yaml)
yaml
Copy
Edit
output_format: pdf
file_format: camel
rename_original: true
two_page_scan: false
template_dir: template_dir
keyword_file: ocr_keywords.xlsx
poppler_path: C:/Poppler/bin
preprocess:
grayscale: false
rotate: true
use_template_fallback: true
template_threshold: 0.85
👨‍💻 Developer Notes
OCR logic lives in hybrid_ocr.py

Fallback template logic uses OpenCV (matchTemplate)

Output filenames are built from parsed metadata in file names

Logs are stored in /logs/ and /processed/

📦 Requirements
Python 3.9+

paddleocr, pytesseract, pdf2image, openpyxl, opencv-python

Poppler (for PDF image extraction)

🧪 Testing
You can test OCR output and vendor matching by running:

bash
Copy
Edit
python run.py
And passing a config dictionary to run_input(filepath, config).

📧 Support
Issues? Drop a message in the GitHub Issues tab or email dev@yourdomain.com.