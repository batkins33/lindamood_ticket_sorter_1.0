from setuptools import setup, find_packages

setup(
    name="lindamood_sorter",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pytesseract",
        "pdf2image",
        "Pillow",
        "opencv-python",
        "rapidfuzz",
        "pandas",
        "openpyxl",
        "pyyaml",
        "PyPDF2",
    ],
    entry_points={"console_scripts": ["lindamood-sorter=main:main"]},
    package_data={"": ["configs.yaml", "ocr_keywords.xlsx"]},
)
