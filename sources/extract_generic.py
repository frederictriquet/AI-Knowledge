#!/usr/bin/env python3
"""Extracteur « readability » générique pour blogs HTML (hors IBM).

Cible un conteneur de contenu (par défaut .post-content, type Hugo/PaperMod),
absolutise liens et images, convertit en Markdown via pandoc. Préserve TOUT le
contenu, y compris la section References (le sourcing qu'on vient chercher).
"""
import re
import subprocess
import sys
from urllib.parse import urljoin

from bs4 import BeautifulSoup

FALLBACK_SELECTORS = (".post-content", "article", "main", ".entry-content")


def extract(html_path, base_url, selector=None, title_override=None):
    soup = BeautifulSoup(open(html_path, encoding="utf-8").read(), "lxml")
    if title_override:
        title = title_override
    else:
        tnode = soup.select_one(".post-title") or soup.find("h1")
        title = tnode.get_text(strip=True) if tnode else ""

    content = None
    for sel in ([selector] if selector else FALLBACK_SELECTORS):
        if sel:
            content = soup.select_one(sel)
            if content:
                break
    if content is None:
        raise SystemExit(f"contenu introuvable dans {html_path}")

    # purger scripts/styles et ancres de titres (PaperMod : <a class="anchor">#</a>)
    for t in content.find_all(["script", "style", "noscript"]):
        t.decompose()
    for a in content.select("a.anchor"):
        a.decompose()
    # absolutiser les liens
    for a in content.find_all("a", href=True):
        a["href"] = urljoin(base_url, a["href"])
    # images : absolutiser src, ne garder que src+alt (le style casse la conversion pandoc)
    for img in content.find_all("img"):
        src = img.get("src")
        if not src:
            img.decompose(); continue
        alt = img.get("alt", "")
        img.attrs = {"src": urljoin(base_url, src), "alt": alt}

    frag = f"<h1>{title}</h1>\n{content}"
    md = subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=frag, capture_output=True, text=True, check=True,
    ).stdout

    # tidy léger HORS des blocs de code : convertir img/a bruts, retirer divs/span
    out = []
    for seg in re.split(r"(```.*?```)", md, flags=re.S):
        if seg.startswith("```"):
            out.append(seg)
        else:
            out.append(_rawtags_to_md(seg))
    md = re.sub(r"\n{3,}", "\n\n", "".join(out))
    return title, md.strip() + "\n"


def _rawtags_to_md(seg):
    def img_repl(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]*)"', tag)
        alt = re.search(r'alt="([^"]*)"', tag)
        return f"![{alt.group(1) if alt else ''}]({src.group(1) if src else ''})"
    seg = re.sub(r"<img\b[^>]*/?>", img_repl, seg)

    def a_repl(m):
        href = re.search(r'href="([^"]*)"', m.group(1))
        return f"[{m.group(2)}]({href.group(1)})" if href else m.group(2)
    seg = re.sub(r"<a\b([^>]*)>(.*?)</a>", a_repl, seg, flags=re.S)

    seg = re.sub(r"</?(div|span|figure|figcaption|center|br)[^>]*/?>", "", seg)
    return seg


if __name__ == "__main__":
    _, m = extract(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    sys.stdout.write(m)
