#!/usr/bin/env python3.10

# header.py
import subprocess

scripts = [
    "copyRecent2.py",  # COPIES HTML FILES TO JOBFAIRBOOK and RUNS DECKTAPE
    # "spl.py",  # cuts in half
    "combPy.py",  # combines 1 2 3 splits #NB EDITED TO NOT SPLIT
    "pgNum.py",  # imposes page umbers on bottom of document
    "scale.py",  # scales non us-letter document to us letter (needs work)
    # "rotate.py",  # scales non us-letter document to us letter (needs work)
    ## "combineFrontMatterAndBook.py",  # staples toc and main book
    "trim.py",
]

for script in scripts:
    print(f"\n--- Running {script} ---\n")
    subprocess.run(["python3", script], check=True)

print("\n--- Running latexmk ---\n")
subprocess.run(["latexmk", "impose.ltx", "--pdf"], check=True)
