import fitz  # PyMuPDF

doc = fitz.open("03.pdf")
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

new_doc.save("03_split.pdf")
new_doc.close()
doc.close()

