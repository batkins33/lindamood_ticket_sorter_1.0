from PIL import Image
from processor import run


def test_run_single_processes_pages(monkeypatch, tmp_path):
    tmp_file = tmp_path / 'sample.png'
    Image.new('RGB', (10, 10), 'white').save(tmp_file)

    processed = {}

    def fake_process_pages(pages, filepath, config, suffix=""):
        processed['pages'] = list(pages)
        processed['filepath'] = filepath
        return ['out.pdf']

    monkeypatch.setattr(run, 'process_pages', fake_process_pages)
    monkeypatch.setattr(run, 'read_text', lambda image=None: {'text': 'dummy', 'confidence': 1.0})

    config = {
        'poppler_path': '',
        'rename_original': False,
        'two_page_scan': False,
    }

    logs = run._run_single(tmp_file, config)

    assert processed['pages'], 'process_pages should receive pages'
    assert logs == [(tmp_file.name, 1, config.get('ocr_engine', 'tesseract'), 'dummy')]
