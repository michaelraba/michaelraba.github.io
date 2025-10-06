import fitz  # PyMuPDF

# Load the imposed PDF file
# input_pdf_path = "merged_output_letter_flipped.pdf"
input_pdf_path = "impose.pdf"
doc = fitz.open(input_pdf_path)

# Define creep parameters
signature_size = 16  # pages per signature
creep_per_sheet_mm = 0.25  # creep per sheet in mm
creep_per_sheet_pt = creep_per_sheet_mm * 2.83465  # convert mm to points

# Create a new PDF to store adjusted pages
new_doc = fitz.open()

# Apply creep adjustment by copying pages with horizontal shift
for i in range(len(doc)):
    signature_index = i // signature_size
    sheet_index = i % signature_size
    # Calculate creep offset: pages closer to center get more offset
    if sheet_index < signature_size // 2:
        creep_offset = (signature_size // 2 - sheet_index) * creep_per_sheet_pt
    else:
        creep_offset = (sheet_index - signature_size // 2) * creep_per_sheet_pt

    # Left pages (even index) shift right, right pages (odd index) shift left
    shift = creep_offset if i % 2 == 0 else -creep_offset

    # Create a new page and draw the original page with horizontal shift
    orig_page = doc[i]
    rect = orig_page.rect
    new_page = new_doc.new_page(width=rect.width, height=rect.height)
    new_page.show_pdf_page(rect + (shift, 0, shift, 0), doc, i)

# Save the adjusted PDF
output_pdf_path = "creep.pdf"
new_doc.save(output_pdf_path)
new_doc.close()
doc.close()

print(f"Creep spacing applied and saved to {output_pdf_path}")
