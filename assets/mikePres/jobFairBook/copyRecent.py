#!/usr/bin/env python3.10

# copy_and_pdf.py
# copies html files to dir jobfairbook
# then converts them to pdf with py package decktape

import shutil
import subprocess
from pathlib import Path

# define source files
src_files = [
    Path("../603talk/603fp.html"),
    Path("../510finalProj/510fp.html"),
    Path("../qme.html"),
]

# define destination directory
dst_dir = Path("./jobFairBook")
dst_dir.mkdir(parents=True, exist_ok=True)  # make sure it exists

# copy each file
for src in src_files:
    dst = dst_dir / src.name
    print(f"Copying {src} -> {dst}")
    shutil.copy2(src, dst)

print("Copy done.")

# run decktape on each copied HTML file
for src in src_files:
    html_file = dst_dir / src.name
    pdf_file = html_file.with_suffix(".pdf")  # same name, but .pdf
    print(f"Running DeckTape on {html_file} -> {pdf_file}")
    subprocess.run(["decktape", "reveal", str(html_file), str(pdf_file)], check=True)

print("All PDFs generated.")
