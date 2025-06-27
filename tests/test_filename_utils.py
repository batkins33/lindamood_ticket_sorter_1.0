from processor.filename_utils import parse_input_filename_fuzzy


def test_parse_input_filename_fuzzy():
    result = parse_input_filename_fuzzy(
        "24-105_2025-04-18_Flexbase_ZoneE_SouthFill.pdf"
    )

    assert result["JOB_ID"] == "24-105"
    assert result["DATE"] == "2025-04-18"
    assert result["MATERIAL"] == "Flexbase"
    assert result["SOURCE"] == "Zonee"
    assert result["DESTINATION"] == "Southfill"
