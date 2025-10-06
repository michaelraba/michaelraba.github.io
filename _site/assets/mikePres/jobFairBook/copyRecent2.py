#!/usr/bin/env python3.10

#!/usr/bin/env python3.10

# pdf_from_html.py
# runs DeckTape on HTML files in their original location
# then copies the generated PDFs to ./jobFairBook

import shutil
import subprocess
from pathlib import Path

# define source HTML files
src_files = [
    Path("../603talk/603fp.html"),
    Path("../510finalProj/510fp.html"),
    Path("../qme.html"),
]

# define destination directory for PDFs
dst_dir = Path("./jobFairBook")
dst_dir.mkdir(parents=True, exist_ok=True)  # make sure it exists

for html_file in src_files:
    # output PDF path (in the same folder as the HTML initially)
    pdf_file = html_file.with_suffix(".pdf")

    print(f"Running DeckTape on {html_file} -> {pdf_file}")
    subprocess.run(["decktape", "reveal", str(html_file), str(pdf_file)], check=True)

    # copy the generated PDF to the jobFairBook folder
    dst_pdf = dst_dir / pdf_file.name
    print(f"Copying {pdf_file} -> {dst_pdf}")
    shutil.copy2(pdf_file, dst_pdf)

print("All PDFs generated and copied to jobFairBook.")
