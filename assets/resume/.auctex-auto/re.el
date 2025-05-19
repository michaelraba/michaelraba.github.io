(TeX-add-style-hook
 "re"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "letterpaper" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fullpage" "empty") ("color" "usenames" "dvipsnames") ("hyperref" "hidelinks") ("babel" "english")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "glyphtounicode"
    "article"
    "art11"
    "latexsym"
    "fullpage"
    "titlesec"
    "marvosym"
    "color"
    "verbatim"
    "enumitem"
    "hyperref"
    "fancyhdr"
    "babel"
    "tabularx")
   (TeX-add-symbols
    '("resumeSubItem" 1)
    '("resumeSubheading" 4)
    '("resumeItem" 1)
    "resumeSubHeadingListStart"
    "resumeSubHeadingListEnd"
    "resumeItemListStart"
    "resumeItemListEnd"))
 :latex)

