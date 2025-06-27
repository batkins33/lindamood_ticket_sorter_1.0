# PATCHED: utils/ocr_paddle.py

import logging

import cv2
import numpy as np

try:
    from paddleocr import PaddleOCR
    _paddle_ocr = PaddleOCR(use_angle_cls=True, lang='en')
    logging.info("✅ PaddleOCR initialized successfully.")
except ImportError:
    PaddleOCR = None  # <--- add this to silence inspection warnings
    _paddle_ocr = None
    logging.warning("⚠️ PaddleOCR not installed or failed to initialize.")



def read_text_paddle(pil_img, **kwargs):
    if _paddle_ocr is None:
        raise RuntimeError("PaddleOCR is not available.")

    try:
        if pil_img.mode != "RGB":
            pil_img = pil_img.convert("RGB")

        image_np = np.array(pil_img)
        image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        result = _paddle_ocr.ocr(image_cv, cls=True)

        if not result:
            return {"engine": "paddleocr", "text": "", "confidence": 0.0}

        all_text = []
        for block in result or []:
            for line in block or []:
                if line and len(line) > 1:
                    text = line[1][0]
                    all_text.append(text)

        return {
            "engine": "paddleocr",
            "text": "\n".join(all_text),
            "confidence": 1.0  # PaddleOCR doesn't return confidence at line-level in this mode
        }

    except Exception as e:
        logging.exception("❌ PaddleOCR exception occurred")
        raise RuntimeError(f"PaddleOCR failed: {e}")
