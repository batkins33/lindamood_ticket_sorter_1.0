### UPDATED FILE: utils/ocr_wrapper.py

import logging

from utils.ocr_paddle import read_text_paddle, _paddle_ocr

is_paddle_available = _paddle_ocr is not None


def read_text(image, **kwargs):
    """
    Unified OCR interface using only PaddleOCR.

    Args:
        image (PIL.Image): The image to OCR.
        kwargs: Optional arguments for PaddleOCR.

    Returns:
        dict: {"engine": "paddleocr", "text": str, "confidence": float}
    """
    if not is_paddle_available:
        raise RuntimeError("PaddleOCR is not available.")

    try:
        return read_text_paddle(image, **kwargs)
    except Exception as e:
        logging.error(f"❌ PaddleOCR processing failed: {e}")
        raise
