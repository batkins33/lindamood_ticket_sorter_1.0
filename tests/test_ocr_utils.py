from processor.filename_utils import (
    format_output_filename,
    format_output_filename_camel,
)


def test_format_output_filename_caps():
    meta = {
        "JOB_ID": "24-105",
        "DATE": "2025-04-18",
        "MATERIAL": "FLEXBASE",
        "SOURCE": "ZONEE",
        "DESTINATION": "SOUTHFILL",
    }
    name = format_output_filename("BIGCITY", 10, meta, "pdf")
    assert name == "24-105_2025-04-18_BIGCITY_FLEXBASE_ZONEE_SOUTHFILL_10.pdf"


def test_format_output_filename_camel_lower():
    meta = {
        "JOB_ID": "24-105",
        "DATE": "2025-04-18",
        "MATERIAL": "Flexbase",
        "SOURCE": "ZoneE",
        "DESTINATION": "SouthFill",
    }
    # Simulate "file_format: lower" configs
    lower_format = lambda v, p, m, f: format_output_filename_camel(v, p, m, f).lower()
    name = lower_format("BigCity", 10, meta, "pdf")
    assert name == "24-105_2025-04-18_bigcity_flexbase_zonee_southfill_10.pdf"
