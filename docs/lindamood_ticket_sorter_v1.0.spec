# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

block_cipher = None

project_root = Path(__file__).parent

a = Analysis(
    ['gui.py'],
    pathex=[str(project_root)],
    binaries=[],
    datas=[
        ('ocr_keywords.xlsx', '.'), 
        ('config.yaml', '.'), 
        ('template_dir/*', 'template_dir')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ticket_sorter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ticket_sorter'
)
