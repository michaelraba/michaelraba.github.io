# Website update (October 30, 2026)

This zip holds only the files that were changed or added, at their paths in the
repository. Unzip it into the root of your `michaelraba.github.io` folder
(say yes to overwrite), then commit and push. Delete this CHANGES.md before
committing, or leave it; it isn't linked anywhere.

## New
- `_pages/projects.md`: new Projects page at /projects/ (the old /talks/ and /portfolio/ links redirect here).
  Project write-ups with images, tools, links to slide decks, model files and the interactive 3D ball-on-beam model.
- `assets/css/projects.css`: styles for project cards, buttons and the skills list.
- `images/projects/*.png`: thumbnails for each project (ball-on-beam render made from your GLB model).
- `assets/resume/Michael_Raba_Resume.tex` / `.pdf`: rewritten one-page resume.

## Changed
- `_pages/about.md`: homepage rewritten (intro, buttons, featured project cards, skills, "Currently").
- `_pages/cv.md`: resume page now has a download button, the embedded PDF and a text version.
- `_pages/sitemap.md`: short, curated sitemap instead of the auto list that showed template pages.
- `_config.yml`: site title and description, sidebar bio, social-share image; template sample pages
  (Blog Post 1-4, Talk 1-3, Teaching 1-2, Portfolio item 1-2, Markdown, Terms, etc.) are no longer published.
- `_data/navigation.yml`: Projects menu link points to /projects/.
- `_includes/head/custom.html`: loads projects.css.
- `assets/resume/F2025cv.pdf`: replaced with the new resume so old links show the current version.
- Slide decks (`msc.html`, `510fp.html`, `603fp.html`, `qme.html`) and their `.org` sources:
  "MSc Candidate" updated to MSc, and typo fixes (Absorbant, Simlab, Constituative, Crosssection, betwen, Klassik).
- `smallPort.tex` / `.org`: typo fixes. The poster PDF itself was NOT rebuilt (missing LaTeX packages here),
  so re-export it on your machine to get the fixes into the PDF.

## Building the resume
The .tex uses your existing `mcdowellcv.cls`. Build it with LuaLaTeX, as you did before:
`lualatex Michael_Raba_Resume.tex`
