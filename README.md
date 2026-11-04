# Yelyzaveta Zalizko: portfolio site

Plain static site (HTML, CSS, a little JavaScript). No framework, nothing to install to view or host it.

## Preview locally
```
cd portfolio-site
python -m http.server 8000
```
Open http://localhost:8000

## Edit content
Text, project order, image lists and contact details all live in `_build/build.py`
(see the `CONFIG` and `PROJECTS` sections). After editing, regenerate the pages:
```
python _build/build.py
```
(needs Python and `pip install pillow`)

- Show a phone number: fill in `PHONE` and set `SHOW_PHONE = True`.
- Add an artwork: put `name-t.webp` (about 900px wide) and `name-f.webp` (about 2000px wide) in `img/`, then add `("name", "alt text")` to a project's `items`.
- Colors, fonts and spacing: `css/style.css` (variables at the top).

## Publish on GitHub Pages
1. Create an empty repo on github.com (name it `<username>.github.io` for a root address).
2. Push this folder's contents to the `main` branch.
3. Repo Settings, Pages, Source: "Deploy from a branch", `main` / root.
