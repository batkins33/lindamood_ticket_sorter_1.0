import os

import numpy as np
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr


def initialize_paddleocr(use_gpu=False):
    print("Initializing PaddleOCR...")
    ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=use_gpu)
    print("PaddleOCR initialized ✅")
    return ocr


def test_ocr_on_image(ocr, image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    result = ocr.ocr(image_path, cls=True)

    for idx, line in enumerate(result[0]):
        text = line[1][0]
        confidence = line[1][1]
        print(f"[{idx+1}] Text: {text} | Confidence: {confidence:.2f}")

    # Optional: Show image with OCR boxes
    image = Image.open(image_path).convert('RGB')
    boxes = [elements[0] for elements in result[0]]
    txts = [elements[1][0] for elements in result[0]]
    scores = [elements[1][1] for elements in result[0]]
    image_with_boxes = draw_ocr(np.array(image), boxes, txts, scores)
    Image.fromarray(image_with_boxes).show()


if __name__ == "__main__":
    # Test image (replace with your own local image path)
    image_path = "test_image.jpg"

    try:
        ocr = initialize_paddleocr(use_gpu=False)
        test_ocr_on_image(ocr, image_path)
    except Exception as e:
        print(f"❌ Error: {e}")

