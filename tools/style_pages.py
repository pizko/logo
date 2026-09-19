#!/usr/bin/env python3
"""Подключает шрифт Onest и clay-pages.css ко всем внутренним страницам (идемпотентно)."""
import pathlib
SRC = pathlib.Path(__file__).resolve().parent.parent / "src"
TAG = ('<link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />'
       '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&display=swap" />'
       '<link rel="stylesheet" href="assets/css/clay-pages.css?v=2" />')
n = 0
for f in sorted(SRC.glob("*.html")):
    if f.name == "index.html":
        continue
    s = f.read_text()
    s = s.replace("document-carousel.css?v=20260809", "document-carousel.css")
    s = s.replace("sidorova.jpg?v=20260804", "sidorova.jpg")
    if "clay-pages.css" not in s:
        s = s.replace("</head>", TAG + "\n</head>", 1)
        n += 1
    f.write_text(s)
print("страниц подключено:", n)
