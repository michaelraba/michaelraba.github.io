
from PyPDF2 import PdfMerger

def merge_pdfs(toc_file, main_file, output_file):
    merger = PdfMerger()

    # Add TOC first
    merger.append(toc_file)

    # Then add the main content
    merger.append(main_file)

    # Write out final file
    merger.write(output_file)
    merger.close()

if __name__ == "__main__":
    toc_file = "toc.pdf"
    main_file = "merged_output_letter.pdf"
    output_file = "final_book.pdf"

    merge_pdfs(toc_file, main_file, output_file)
    print(f"Merged PDF saved as {output_file}")
