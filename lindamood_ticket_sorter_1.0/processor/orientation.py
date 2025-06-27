def correct_image_orientation(pil_img):
    try:
        osd = pytesseract.image_to_osd(pil_img)
        rotation_match = re.search(r"Rotate: (\d+)", osd)
        if rotation_match:
            rotation = int(rotation_match.group(1))
            if rotation == 90:
                return pil_img.rotate(-90, expand=True)
            elif rotation == 180:
                return pil_img.rotate(180, expand=True)
            elif rotation == 270:
                return pil_img.rotate(-270, expand=True)
    except pytesseract.TesseractError as e:
        print(f"Tesseract error during orientation detection: {e}")
    except Exception as e:
        print(f"Unexpected error in orientation correction: {e}")

    return pil_img


def extract_ticket_number(pil_img):
    text = pytesseract.image_to_string(pil_img)
    text = text.replace("\n", " ").strip()
    match = re.search(r"(A[\s\-:]?\d{5,})", text, re.IGNORECASE)
    if match:
        ticket_number = match.group(1).replace(" ", "").replace("-", "")
        return ticket_number
    # """
    # page_image: full page (RGB or grayscale) as np.array
    # template_dict: {"VENDOR": [template_image1, template_image2, ...]}
    # Returns: best matched vendor and score
    # """


