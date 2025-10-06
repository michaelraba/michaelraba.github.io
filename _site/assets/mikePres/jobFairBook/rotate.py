import PyPDF2


def rotate_pdf(input_file, output_file, rotation=90):
    # Open the input PDF
    with open(input_file, "rb") as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()

        # Rotate each page
        for page in reader.pages:
            page = page.rotate(rotation)  # PyPDF2 v3+ API
            writer.add_page(page)

        # Save to output PDF
        with open(output_file, "wb") as outfile:
            writer.write(outfile)


if __name__ == "__main__":
    rotate_pdf("merged_output_letter.pdf", "merged_output_letter_flipped.pdf", 90)
