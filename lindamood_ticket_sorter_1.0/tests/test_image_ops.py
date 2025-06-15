from PIL import Image

from processor import image_ops


def test_extract_ticket_number():
    img = Image.new("RGB", (200, 100), "white")
    number = image_ops.extract_ticket_number(img)
    assert isinstance(number, str)
