
import fitz  # PyMuPDF

def scale_to_letter(input_file, output_file):
    # Letter size in points (1 in = 72 pt)
    letter_width, letter_height = 612, 792

    src_doc = fitz.open(input_file)
    dst_doc = fitz.open()

    for page in src_doc:
        rect = page.rect
        orig_width, orig_height = rect.width, rect.height

        # Scale factor (preserve aspect ratio)
        scale_x = letter_width / orig_width
        scale_y = letter_height / orig_height
        scale = min(scale_x, scale_y)

        # New scaled dimensions
        new_width = orig_width * scale
        new_height = orig_height * scale

        # Centering offsets
        x_offset = (letter_width - new_width) / 2
        y_offset = (letter_height - new_height) / 2

        # Create a blank Letter page
        new_page = dst_doc.new_page(width=letter_width, height=letter_height)

        # Define target rectangle
        target_rect = fitz.Rect(
            x_offset, y_offset, x_offset + new_width, y_offset + new_height
        )

        # Insert source page into target rect (scales automatically)
        new_page.show_pdf_page(target_rect, src_doc, page.number)

    dst_doc.save(output_file)

if __name__ == "__main__":
    input_file = "merged_output_numbered.pdf"
    output_file = "merged_output_letter.pdf"
    scale_to_letter(input_file, output_file)
    print(f"Scaled PDF saved as {output_file}")
