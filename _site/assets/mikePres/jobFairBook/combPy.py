#!/usr/bin/env python3.10

import fitz  # PyMuPDF

# list of PDFs to merge
# pdf_files = [
#    "./jobFairBook/510fp_split.pdf",
#    "./jobFairBook/603fp_split.pdf",
#    "./jobFairBook/qme_split.pdf",
# ]

pdf_files = [
    "./jobFairBook/510fp.pdf",
    "./jobFairBook/603fp.pdf",
    "./jobFairBook/qme.pdf",
]

merged = fitz.open()

# Add a blank first page (US Letter)
first_page_width = 612  # US Letter width in points
first_page_height = 792  # US Letter height in points
merged.new_page(width=first_page_width, height=first_page_height)

# Insert each PDF in order
for file in pdf_files:
    doc = fitz.open(file)
    merged.insert_pdf(doc)
    doc.close()

# Save the merged PDF
merged.save("merged_output.pdf")
merged.close()

print("ran combPy.py: merged PDFs with blank first page")
