#!/usr/bin/env python3
"""Extrait le corps d'un article IBM Think en Markdown propre.

- Récupère le titre (leadspace) et les blocs de contenu (cms-richtext).
- Code inline <cds-code-snippet type="inline"> -> `code`.
- Blocs de code (<cds-code-snippet> multi et <pre>) -> ```lang fence```,
  via des marqueurs réinjectés après pandoc (langage deviné par heuristique).
- Supprime masthead, navigation, leadspace, cartes promo / experience
  fragments, bios auteurs, modules de partage, CTA de bas de page.
"""
import html as _html
import re
import subprocess
import sys

from bs4 import BeautifulSoup

# Sous-arbres supprimés si une de leurs classes contient l'un de ces fragments.
BOILER = (
    "masthead", "cmp-side-navigation", "side-nav-section",
    "cmp-leadspace", "leadspace",
    "card-list-item", "cds--card", "card-group", "xfpage", "xf-content-height",
    "cmp-experiencefragment", "cta-section", "ibmcom-next-steps",
    "cds--cta-block", "author-signature", "cmp-author-signature",
    "share-module", "cds-btn--share-module", "breadcrumb", "dotcom-shell",
    "consent", "cookie", "newsletter", "subscribe",
)
NEWSLETTER = ("## Les dernières tendances", "## Merci")
MARK = "@@CODEBLOCK_{}@@"


def guess_lang(code):
    """Devine le langage d'un bloc pour la coloration syntaxique."""
    c = code.strip()
    head = c.splitlines()[0] if c else ""
    if re.search(r"^\s*(from |import |def |class |async def |@|print\()", c, re.M) \
            or "self." in c:
        return "python"
    if ("{" in c or "[" in c) and re.search(r'"\s*:', c):
        return "json"
    if re.match(r"^\s*(pip|cd |mkdir|source |export |python3?|git |curl|uv |"
                r"docker|npm|brew|chmod|sudo|\./|fastmcp|ollama)\b", head):
        return "bash"
    return ""


def collect_code(soup, codes):
    """Inline -> <code> ; blocs (<cds-code-snippet> multi, <pre>) -> marqueur."""
    for cs in soup.find_all("cds-code-snippet"):
        inner = re.sub(r"<br\s*/?>\s*", "\n", cs.decode_contents())
        text = _html.unescape(re.sub(r"<[^>]+>", "", inner)).strip("\n")
        if cs.get("type") == "inline":
            node = soup.new_tag("code")
            node.string = text.strip()
            cs.replace_with(node)
        else:
            cs.replace_with(_marker(soup, codes, text))
    for pre in soup.find_all("pre"):
        text = _html.unescape(pre.get_text()).strip("\n")
        pre.replace_with(_marker(soup, codes, text))


def _marker(soup, codes, text):
    p = soup.new_tag("p")
    p.string = MARK.format(len(codes))
    codes.append(text)
    return p


def extract_fragment(html, codes):
    soup = BeautifulSoup(html, "lxml")
    h1 = (
        soup.select_one(".cmp-leadspace__content-header h1")
        or soup.select_one(".cmp-leadspace__heading")
        or soup.find("h1")
    )
    title = h1.get_text(strip=True) if h1 else ""

    collect_code(soup, codes)

    for tag in soup.find_all(["script", "style", "svg", "noscript",
                              "header", "footer", "nav", "form"]):
        tag.decompose()
    for el in soup.find_all(class_=True):
        if el.decomposed or not el.attrs:
            continue
        cls = " ".join(el.get("class") or [])
        if any(b in cls for b in BOILER):
            el.decompose()

    # Colonne principale de l'article (texte + code + listes + tableaux, dans
    # l'ordre). À défaut, on retombe sur les blocs cms-richtext de premier niveau.
    col = soup.select_one(".body-article-8") or soup.select_one(".article-content-slot")
    if col is not None:
        body = str(col)
    else:
        blocks = [
            rt for rt in soup.select(".cms-richtext")
            if not rt.find_parent(class_="cms-richtext")
        ]
        body = "\n".join(str(b) for b in blocks)
    parts = [f"<h1>{title}</h1>"] if title else []
    parts.append(body)
    return "\n".join(parts), title


def to_markdown(fragment):
    return subprocess.run(
        ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
        input=fragment, capture_output=True, text=True, check=True,
    ).stdout


def reinject_code(md, codes):
    for i, code in enumerate(codes):
        fence = f"```{guess_lang(code)}\n{code}\n```"
        md = md.replace(MARK.format(i), fence)
    return md


def _strip_html(seg):
    """Retire balises HTML résiduelles et images data-uri (hors code)."""
    seg = re.sub(r"!\[\]\(data:[^)]*\)", "", seg)
    seg = re.sub(r"</?[a-zA-Z][^>]*>", "", seg)
    return seg


def tidy(md, title):
    out, skip = [], False
    for l in md.split("\n"):
        if any(l.startswith(p) for p in NEWSLETTER):
            skip = True
            continue
        if skip:
            if l.startswith("#"):
                skip = False
            else:
                continue
        if title and l.strip() in (f"## {title}", f"### {title}"):
            continue
        out.append(l)
    text = "\n".join(out)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def convert(path):
    codes = []
    fragment, title = extract_fragment(open(path, encoding="utf-8").read(), codes)
    md = to_markdown(fragment)
    md = _strip_html(md)            # sûr : le code est encore sous forme de marqueurs
    md = reinject_code(md, codes)
    return tidy(md, title)


if __name__ == "__main__":
    sys.stdout.write(convert(sys.argv[1]))
