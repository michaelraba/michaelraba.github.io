import fitz  # PyMuPDF

doc = fitz.open("merged_output.pdf")
font_size = 12
margin = 20

for i, page in enumerate(doc):
    text = str(i + 1)
    rect = page.rect
    # Slightly larger rectangle near bottom-right
    textbox = fitz.Rect(rect.width - 100, rect.height - 40, rect.width - margin, rect.height - 10)
    page.insert_textbox(
        textbox,
        text,
        fontsize=font_size,
        fontname="helvetica",   # safer than "helv"
        color=(0, 0, 0),
        align=fitz.TEXT_ALIGN_RIGHT
    )

doc.save("merged_output_numbered.pdf")
doc.close()

