#!/usr/bin/env python3.10

import fitz  # PyMuPDF
from pathlib import Path

# list of PDF files to split
pdf_files = [
    Path("./jobFairBook/qme.pdf"),
    Path("./jobFairBook/510fp.pdf"),  # example: from 510finalProj
    Path("./jobFairBook/603fp.pdf"),
]

for pdf_file in pdf_files:
    split_file = pdf_file.with_stem(pdf_file.stem + "_split")
    print(f"Splitting {pdf_file} -> {split_file}")

    doc = fitz.open(pdf_file)
    new_doc = fitz.open()

    for page in doc:
        rect = page.rect
        mid_x = rect.width / 2

        left_rect = fitz.Rect(0, 0, mid_x, rect.height)
        right_rect = fitz.Rect(mid_x, 0, rect.width, rect.height)

        left_page = new_doc.new_page(width=mid_x, height=rect.height)
        left_page.show_pdf_page(left_page.rect, doc, page.number, clip=left_rect)

        right_page = new_doc.new_page(width=mid_x, height=rect.height)
        right_page.show_pdf_page(right_page.rect, doc, page.number, clip=right_rect)

    new_doc.save(split_file)
    new_doc.close()
    doc.close()

print("All PDFs split successfully.")
