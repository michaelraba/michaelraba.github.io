
import fitz  # PyMuPDF

pdf_files = ["01_split.pdf", "02_split.pdf", "03_split.pdf"]
merged = fitz.open()

for file in pdf_files:
    doc = fitz.open(file)
    merged.insert_pdf(doc)
    doc.close()

merged.save("merged_output.pdf")
merged.close()

