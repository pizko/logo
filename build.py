#!/usr/bin/env python3
"""src/ → docs/ (GitHub Pages, тестовая копия).

В копии: noindex, без Яндекс.Метрики и метки q_status — чтобы не портить статистику и индекс
настоящего сайта лого-будущее.рф. В src/ всё остаётся как для боевого домена.

  python3 tools/make_home.py     # главная из шаблона
  python3 tools/style_pages.py   # стиль внутренних страниц
  python3 build.py               # тестовая копия в docs/
"""
import pathlib, re, shutil

ROOT = pathlib.Path(__file__).resolve().parent
SRC, OUT = ROOT / "src", ROOT / "docs"
if OUT.exists():
    shutil.rmtree(OUT)
shutil.copytree(SRC, OUT, ignore=shutil.ignore_patterns(".DS_Store", "_*"))
for f in OUT.glob("*.html"):
    s = f.read_text()
    s = re.sub(r"\s*<!-- Yandex\.Metrika counter -->.*?<!-- /Yandex\.Metrika counter -->", "", s, flags=re.S)
    s = s.replace('<script src="/assets/js/qmark.js" defer></script>', "")
    # на части страниц счётчик вставлен без комментариев-маркеров
    s = re.sub(r"<script[^>]*>(?:(?!</script>).)*mc\.yandex\.ru(?:(?!</script>).)*</script>", "", s, flags=re.S)
    s = re.sub(r"<noscript>(?:(?!</noscript>).)*mc\.yandex\.ru(?:(?!</noscript>).)*</noscript>", "", s, flags=re.S)
    s = re.sub(r'<meta name="robots" content="[^"]*"\s*/?>', "", s)
    s = s.replace("</head>", '<meta name="robots" content="noindex, nofollow" />\n</head>', 1)
    f.write_text(s)
(OUT / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
(OUT / ".nojekyll").write_text("")
bad = [f.name for f in OUT.glob("*.html") if "mc.yandex.ru" in f.read_text()]
print("docs/ собран, страниц:", len(list(OUT.glob("*.html"))), "| Метрика осталась в:", bad or "нигде")
