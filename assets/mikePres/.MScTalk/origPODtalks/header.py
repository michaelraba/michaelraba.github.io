#!/usr/bin/env python3.10

# header.py
import subprocess

scripts = [
    "spl.py",  # cuts in half
    "combPy.py",  # combines 1 2 3 splits
    "pgNum.py",  # imposes page umbers on bottom of document
    "scale.py",  # scales non us-letter document to us letter (needs work)
    "combineFrontMatterAndBook.py",  # staples toc and main book
]

for script in scripts:
    print(f"\n--- Running {script} ---\n")
    subprocess.run(["python3", script], check=True)
