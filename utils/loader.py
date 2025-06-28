import json
import os
import logging
from pathlib import Path

import pandas as pd
import yaml
from schema import Schema, And, Use, SchemaError

PROJECT_ROOT = Path(__file__).resolve().parents[1]

_ocr_configs_cache = {}


def _resolve_path(path: str) -> Path:
    p = Path(path)
    return p if p.is_absolute() else PROJECT_ROOT / p


def load_configs(path: str = "configs.yaml"):
    path = _resolve_path(path)
    with open(path, "r") as file:
        raw = os.path.expandvars(file.read())
        configs = yaml.safe_load(raw)

    schema = Schema(
        {
            "output_format": And(Use(str.lower), lambda s: s in ("pdf", "tif")),
            "file_format": And(
                Use(str.lower), lambda s: s in ("camel", "caps", "lower")
            ),
            # Add more validations if needed, e.g.:
            # "rename_original": bool,
            # "two_page_scan": bool,
        }
    )

    try:
        configs = schema.validate(configs)
    except SchemaError as e:
        raise ValueError(f"Invalid configuration: {e}")

    return configs


def load_ocr_configs_from_excel(path: str):
    path = _resolve_path(path)
    mtime = os.path.getmtime(path)
    cached = _ocr_configs_cache.get(path)
    if cached and cached.get("mtime") == mtime:
        return cached["configs"]

    configs = {}
    try:
        df = pd.read_excel(path, engine="openpyxl")
    except Exception as e:
        logging.error(f"Failed to load OCR keyword Excel: {e}")
        return {}

    required_cols = {"vendor name", "vendor type", "ocr match terms"}
    if not required_cols.issubset(set(df.columns.str.lower())):
        logging.error(f"Missing one or more required columns: {required_cols}")
        return {}

    for i, row in df.iterrows():
        try:
            name = str(row["vendor name"]).strip()
            vtype = str(row["vendor type"]).strip().lower()
            keywords = [
                kw.strip()
                for kw in str(row["ocr match terms"]).split(",")
                if kw.strip()
            ]
            if not (name and vtype and keywords):
                logging.warning(f"Skipping row {i + 2} due to empty fields: {row}")
                continue
            configs[name] = {
                "vendor_type": vtype,
                "keywords": keywords,
            }
        except Exception as e:
            logging.warning(f"Failed to parse row {i + 2}: {e}")
            continue

    _ocr_configs_cache[str(path)] = {"configs": configs, "mtime": mtime}
    return configs


def load_ocr_keywords(filepath: str):
    path = _resolve_path(filepath)
    if path.suffix.lower() == ".json":
        with open(path, "r") as f:
            return json.load(f)
    else:
        keyword_dict = {}
        df = pd.read_excel(path, engine="openpyxl")
        for _, row in df.iterrows():
            company = str(row.get("company name", "")).strip()
            raw_terms = str(row.get("ocr match terms", "")).strip()
            terms = [t.lower().strip() for t in raw_terms.split(",") if t.strip()]
            if company and terms:
                keyword_dict[company] = terms
        return keyword_dict


def load_templates(template_dir: str):
    from collections import defaultdict
    import os
    import cv2
    from pathlib import Path
    template_dir = _resolve_path(template_dir)

    templates = defaultdict(list)

    for root, _, files in os.walk(template_dir):
        vendor = Path(root).name.lower()
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".tif", ".tiff")):
                full_path = os.path.join(root, file)
                img = cv2.imread(full_path, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    logging.warning(f"Failed to load template: {full_path}")
                else:
                    logging.info(f"Loaded template for vendor '{vendor}': {file}")
                    templates[vendor].append(img)

    logging.info(f"Total vendors loaded: {len(templates)}")
    return templates
