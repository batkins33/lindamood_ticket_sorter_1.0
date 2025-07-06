from processor import hybrid_ocr


def test_process_pages_groups_and_exports(monkeypatch, tmp_path):
    img_a = b'image_a'
    img_b = b'image_b'
    pages = [img_a, img_b]

    def fake_process_single_page(args):
        i, page, filepath, config, templates, ocr_config, expected_vendor, cache = args
        vendor = 'VendorA' if i == 0 else 'VendorB'
        return {
            'page': i,
            'page_image': page,
            'vendor': vendor,
            'matched': True,
            'ticket': 'T',
            'method': 'OCR',
            'keyword': 'kw',
            'rotated': False,
            'grayscale': False,
            'ocr_score': 1.0,
            'expected_vendor': '',
            'preview': '',
            'ocr_text': 'text'
        }, f'hash{i}'

    exported = {}

    def fake_export_grouped_output(pages_by_vendor, fmt, meta, fp, cfg):
        exported['pages'] = {k: list(v) for k, v in pages_by_vendor.items()}
        return ['out_a.pdf', 'out_b.pdf']

    monkeypatch.setattr(hybrid_ocr, 'process_single_page', fake_process_single_page)
    monkeypatch.setattr(hybrid_ocr, 'export_grouped_output', fake_export_grouped_output)
    monkeypatch.setattr(hybrid_ocr, 'load_templates', lambda *_: {})
    monkeypatch.setattr(hybrid_ocr, 'load_ocr_configs_from_excel', lambda *_: {})
    monkeypatch.setattr(hybrid_ocr, 'parse_input_filename', lambda *_: {
        'JOB_ID': 'JOB',
        'DATE': '2020-01-01',
        'MATERIAL': 'MAT',
        'SOURCE': 'SRC',
        'DESTINATION': 'DST'
    })

    config = {
        'template_dir': 'templates',
        'keyword_file': 'keywords.xlsx',
        'output_format': 'pdf',
        'num_workers': 1,
        'preprocess': {'grayscale': False, 'rotate': False}
    }

    out = hybrid_ocr.process_pages(pages, tmp_path / 'file.pdf', config)

    assert exported['pages']['VendorA'][0] == img_a
    assert exported['pages']['VendorB'][0] == img_b
    assert out == ['out_a.pdf', 'out_b.pdf']
