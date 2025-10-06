import fitz  # PyMuPDF


def trim_pdf(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)

    for page in doc:
        rect = page.rect

        # Adjusted trim values based on visual inspection
        trim_left = 100  # stronger left trim
        trim_right = 72  # keep right trim
        trim_top = 36  # optional
        trim_bottom = 36  # optional

        # Define new rectangle
        new_rect = fitz.Rect(
            rect.x0 + trim_left,
            rect.y0 + trim_bottom,
            rect.x1 - trim_right,
            rect.y1 - trim_top,
        )

        # Apply the new rectangle to the page's MediaBox
        page.set_mediabox(new_rect)

    doc.save(output_pdf)
    doc.close()


# Example usage
trim_pdf("merged_output_letter_flipped.pdf", "trimmed_output.pdf")
