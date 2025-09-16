(TeX-add-style-hook
 "impose"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "pdfpages"))
 :latex)

