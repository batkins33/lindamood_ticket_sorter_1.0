from pathlib import Path

from processor import file_handler


def test_get_dynamic_paths(tmp_path):
    out, log = file_handler.get_dynamic_paths(tmp_path / "input.pdf")
    assert Path(out).exists()
    assert Path(log).exists()


def test_archive_original(tmp_path):
    file = tmp_path / "test.pdf"
    file.write_text("dummy content")
    file_handler.archive_original(str(file))
    assert (tmp_path / "Original Scans" / "test.pdf").exists()
