from utils import loader


def test_load_ocr_keywords_xlsx():
    # This test assumes the keywords file exists at this path
    keywords = loader.load_ocr_keywords("ocr_keywords.xlsx")
    assert isinstance(keywords, dict)
