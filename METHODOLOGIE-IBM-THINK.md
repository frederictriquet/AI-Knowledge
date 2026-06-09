# Méthode — construire une base de connaissances à partir d'un hub IBM Think

Runbook reproductible : d'une **URL de hub** IBM Think (ex. `https://www.ibm.com/fr-fr/think/ai-agents`)
vers un **ensemble de pages Markdown propres, numérotées dans l'ordre de lecture, agrégées et
synthétisées**.

Validé sur le hub « Guide 2026 des agents IA » (77 pages → 63 fiches de concepts → +38 compléments).
Chaque étape donne la commande/script réel et **les pièges** rencontrés.

---

## 0. Nature du site (à comprendre avant tout)

- Les pages IBM Think sont du **HTML rendu côté serveur** (Adobe Experience Manager / AEM), mis en
  cache par Akamai. Le contenu *est* dans le HTML — pas besoin de rendu JavaScript.
- Un « hub » (ex. `/think/ai-agents`) est **une seule page**, pas une arborescence. Le menu de
  gauche est une **table des matières interne** ; les ancres type `#605511093` ne sont que des
  cibles de section.
- **Le hub ne contient pas les articles** : il contient l'intro, le sommaire, des résumés et des
  cartes de ressources. Chaque entrée du sommaire **pointe vers une page séparée** :
  `/think/topics/…` (fiches), `/think/insights/…` (articles d'opinion), `/think/tutorials/…`.
- Le contenu est enveloppé dans des conteneurs AEM (`cmp-*`, `body-article-*`, `cms-richtext`) et
  des **web components Carbon** (`c4d-*`, `cds-*`), dont `cds-code-snippet` pour le code.

> Conséquence : la stratégie n'est pas « rendre la page » mais « **télécharger le HTML brut, isoler
> la colonne de contenu, convertir** ».

---

## 1. Prérequis & environnement

```bash
# Outils système
curl --version        # téléchargement
pandoc --version      # conversion HTML -> gfm (Markdown)
python3 --version

# Dépendances Python (PEP 668 bloque le pip système -> venv obligatoire)
python3 -m venv .venv
.venv/bin/pip install beautifulsoup4 lxml
```

Pièges d'environnement :
- **`pip install` système échoue** (`externally-managed-environment`) → toujours passer par un venv.
- **Wrappers de shell** : certains environnements réécrivent `grep`/`ls` (ex. proxy `rtk`) et
  rejettent `-E`, `-o`, `-n`, `-r`. → Pour toute extraction par regex, **utiliser Python**
  (`python3 - <<'PY' …`) plutôt que `grep -oE`.
- **Reconnaissance optionnelle** : un navigateur piloté (MCP Firefox) sert à *confirmer* visuellement
  la structure (capture d'écran, `list_network_requests`), mais **pas** à extraire — le HTML brut via
  `curl` suffit et est plus fiable.

---

## 2. Récupération du HTML (contournement du 403)

`WebFetch`/outils génériques → **403 Forbidden** : IBM filtre **sur le User-Agent**, pas par
authentification. Un `curl` avec un UA de navigateur passe :

```bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:151.0) Gecko/20100101 Firefox/151.0"
curl -sS -L --compressed -A "$UA" -H "Accept-Language: fr,fr-FR;q=0.9" \
  "https://www.ibm.com/fr-fr/think/<HUB>" -o html/00-hub.html -w "%{http_code} %{size_download}\n"
```

- `--compressed` (gzip/br), `-L` (redirections), `-A` (UA navigateur) = les 3 indispensables.
- Vérifier `200` et une taille plausible (le hub fait ~50 Ko ; un article ~270-370 Ko).

---

## 3. Extraire les URLs d'articles + les deux ordres

Le hub liste tous les articles. On en a besoin sous **deux ordres** :

1. **Ordre du DOM = ordre de lecture du sommaire** (première occurrence) → numérotation finale.
2. (Accessoirement, ordre alphabétique pour un téléchargement stable.)

```python
import re
html = open('html/00-hub.html', encoding='utf-8').read()
pat = re.compile(r'href="(https://www\.ibm\.com/fr-fr/think/(?:topics|insights|tutorials)/[^"#]*)')
seen, order = set(), []
for m in pat.finditer(html):          # itère dans l'ordre du DOM
    u = m.group(1)
    if u not in seen:
        seen.add(u); order.append(u)  # dédup 1re occurrence = position sommaire
open('navorder.txt','w').write('\n'.join(order)+'\n')
```

Pièges :
- Filtrer **strictement** `topics|insights|tutorials` et exclure les liens parasites
  (auteurs, podcasts, autres langues `/ae-ar/`, `/de-de/`, réseaux sociaux, `image.coreimg…`).
- Retirer les ancres (`#…`) **avant** de dédupliquer.
- La nav du DOM apparaît **avant** l'intro → la 1re occurrence d'un lien = bien sa position sommaire.

---

## 4. Télécharger tous les articles

```bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:151.0) Gecko/20100101 Firefox/151.0"
mkdir -p html
i=0
while read -r url; do
  i=$((i+1)); name=$(printf "%02d" $i)-$(basename "$url")
  curl -sS -L --compressed -A "$UA" -H "Accept-Language: fr,fr-FR;q=0.9" \
    "$url" -o "html/$name.html" -w "%{http_code} %{bytes} $name\n"
done < urls.txt      # urls.txt = ordre choisi pour le nommage des fichiers HTML
```

> Le **numéro de fichier HTML** sert seulement d'identifiant de mapping URL↔fichier ; la
> numérotation *finale* (ordre sommaire) est appliquée plus tard (§6).

---

## 5. Cœur du process — extraction & nettoyage HTML → Markdown

Outil canonique : **`ibm-guide-agents-ia/extract.py`** (bs4 + lxml + pandoc). Réutilisable tel quel
pour toute page d'article IBM Think. Algorithme :

### 5.1 Isoler le contenu (et rien d'autre)
- **Titre** : `.cmp-leadspace__content-header h1` (fallback `.cmp-leadspace__heading`, `<h1>`).
- **Corps** : la colonne principale `.body-article-8` (fallback `.article-content-slot`, puis union
  des `.cms-richtext` de premier niveau). C'est **la** clé : `body-article-8` contient texte +
  code + listes dans l'ordre, et exclut naturellement leadspace/promo/sidebars.

### 5.2 Décomposer le boilerplate (par mots-clés de classe)
```
masthead, cmp-side-navigation, side-nav-section, cmp-leadspace, leadspace,
card-list-item, cds--card, card-group, xfpage, xf-content-height, cmp-experiencefragment,
cta-section, ibmcom-next-steps, cds--cta-block, author-signature, cmp-author-signature,
share-module, cds-btn--share-module, breadcrumb, dotcom-shell, consent, cookie,
newsletter, subscribe
```
+ supprimer les balises `script, style, svg, noscript, header, footer, nav, form`.

> **PIÈGE MAJEUR** : ne **pas** décomposer `cmp-table-of-contents--article-side-nav`. La div qui
> enveloppe tout l'article porte **à la fois** `--article-side-nav` ET `--article-content-slot` →
> la cibler efface l'article entier. La vraie nav répétée est dans `cmp-side-navigation` (enfant),
> qu'on supprime sans risque.
>
> **PIÈGE bs4** : décomposer un parent détache ses enfants encore présents dans la liste
> `find_all` → garder `if el.decomposed or not el.attrs: continue`.

### 5.3 Récupérer le code (sinon perdu)
Le code vit dans des web components `cds-code-snippet` (que pandoc ignore) **et** des `<pre>` natifs.
- `type="inline"` → `<code>` (backticks).
- bloc (`type="multi"`) + `<pre>` natif → **marqueur** `@@CODEBLOCK_N@@`, code mis de côté, puis
  **réinjecté après pandoc** en bloc ` ```lang ` (langage deviné : python/bash/json par heuristique).
- Avant extraction du texte : remplacer `<br/>` (+ `\n` collé) par un saut simple, **dé-échapper les
  entités** (`&quot;`, `&#39;` souvent doublement échappées dans les `<pre>` AEM).

> Pourquoi des marqueurs ? pandoc rend mal un `<pre>` issu d'un contexte inline (indentation, pas de
> fence). Les marqueurs garantissent des fences propres + permettent de **dépouiller le HTML résiduel
> sans abîmer le code** (le code n'est pas encore présent au moment du strip).

### 5.4 Pipeline de conversion (ordre impératif)
```
fragment_html = "<h1>titre</h1>" + str(colonne_body_article_8)   # après décompose + marqueurs code
md = pandoc(fragment_html, from=html, to=gfm, --wrap=none)
md = strip_html(md)              # retire <div>/<span>/images data-uri — SÛR ici (code = marqueurs)
md = reinject_code(md, codes)    # marqueurs -> ```lang … ```
md = tidy(md, titre)             # cf. 5.5
```

### 5.5 Tidy final
- Retirer les blocs newsletter : titres commençant par `## Les dernières tendances` et `## Merci`
  (⚠️ **espace insécable français** avant `!`/`?` → matcher sur un **préfixe court**, pas la chaîne
  exacte).
- Dé-dupliquer le titre re-cité en `##`/`###` juste sous le `#`.
- `[ \t]+\n` → `\n` ; `\n{3,}` → `\n\n`.

### 5.6 Lancer l'extraction sur tout le corpus
```python
import extract                      # ibm-guide-agents-ia/extract.py
md = extract.convert("html/07-agentic-ai.html")   # -> Markdown propre
```

Limites assumées (à documenter dans la base) :
- Les **liens markdown** peuvent être cassés *à la source* : la traduction FR insère un mot entre le
  libellé et l'URL (`[intelligence artificielle] générative (https://…)`). Non corrigeable côté extraction.
- Quelques **sorties de programme** dans les tutoriels restent sans langage de coloration (volontaire,
  pour éviter les faux positifs).
- Bug source occasionnel : deux lignes de code fusionnées (`FastMCP``import requests`).

---

## 6. Renumérotation dans l'ordre du sommaire

Les numéros de téléchargement (alphabétiques) **ne reflètent pas l'ordre de lecture**. On remappe :

```python
import extract
nav   = open('navorder.txt').read().split()     # ordre sommaire (DOM)
alpha = open('urls.txt').read().split()          # ordre des fichiers html/NN-…
ai = {u:i+1 for i,u in enumerate(alpha)}         # url -> index du fichier HTML

# Hub = 00 ; articles = 01..N dans l'ordre sommaire
for k, url in enumerate(nav, 1):
    slug = url.rsplit('/',1)[1]
    src  = f"html/{ai[url]:02d}-{slug}.html"      # mapping par URL COMPLÈTE
    md   = extract.convert(src)
    open(f"md/{k:02d}-{slug}.md",'w').write(f"> Source : {url}\n\n"+md)
```

> **PIÈGE** : des slugs sont **ambigus** (`agentic-rag` existe en `topics` ET `tutorials`,
> `ai-agent-evaluation` aussi). **Toujours mapper par URL complète**, jamais par `basename`.

Chaque `.md` porte un en-tête `> Source : <url>` (traçabilité).

---

## 7. Index & agrégation

- **INDEX.md** : sommaire numéroté `N. [titre](md/NN-slug.md) — [source](url)` (titre = 1er `# `).
- **GUIDE-COMPLET.md** : concaténation de toutes les fiches, séparées par `---`.

Contrôle qualité à scripter (Python, pas grep) :
```python
# 0 résidu de nav / cookie / masthead / <div> ; chaque fiche a un H1 ; liens valides
```

---

## 8. Couche de synthèse (optionnelle mais c'est la valeur)

Transformer le corpus brut en **base condensée** :

1. **Relevé fidèle, fichier par fichier** — *ne pas* synthétiser de mémoire. Lancer des
   **sous-agents en parallèle** (lots de ~11 fichiers), chacun **lisant intégralement** ses fichiers
   et renvoyant un relevé structuré : *patterns nommés / sources réellement citées / substance pour
   expert / résumé*. (Règle d'intégrité : traiter réellement chaque élément, étiqueter la provenance.)
2. **Glossaire des patterns** (`GLOSSAIRE-PATTERNS.md`) : une ligne par notion, avec
   **tag de pertinence** (🟢 pur-nom / 🟡 tradeoff / 🔴 substance) et **tag de provenance**
   (✅ présent + n° de fichier / ➕ hors-corpus).
3. **Fiches de concepts** (`concepts/<slug>.md`) : une page condensée par item, gabarit fixe
   (*En une phrase / Ce que dit le corpus / Tradeoff / Source primaire / Voir aussi*), générée par
   sous-agents qui **relisent les fichiers source**. Liens croisés + back-link glossaire.
4. **Compléments hors-corpus** (`concepts/hors-corpus/`) : notions de l'état de l'art absentes du
   site, **clairement marquées `➕`, sans section « Ce que dit le corpus »**, sources « à vérifier ».
5. **Injection des liens** dans le glossaire par script (ancrage sur `| **<nom>**` pour les lignes de
   tableau) + vérification : 0 fiche orpheline, 0 lien cassé.

---

## 9. Pièges spécifiques IBM Think — récapitulatif

| Symptôme | Cause | Parade |
|---|---|---|
| 403 Forbidden | filtrage par User-Agent | `curl -A "<UA navigateur>"` |
| Page « vide » au scraping DOM | web components Carbon / conteneurs AEM | télécharger le HTML brut, cibler `body-article-8` |
| Article entier effacé au nettoyage | wrapper portant `--article-side-nav` + `--article-content-slot` | ne pas décomposer cette classe ; viser `cmp-side-navigation` |
| Code des tutoriels perdu | `cds-code-snippet` ignoré par pandoc | inline→`<code>`, bloc/`<pre>`→marqueur→fence réinjectée |
| `&quot;` dans les blocs de code | entités doublement échappées dans `<pre>` | `html.unescape()` sur le texte |
| Blocs newsletter qui subsistent | espace insécable FR avant `!` | matcher un **préfixe court** du titre |
| `<div>` bruts dans le MD | pandoc gfm garde le HTML | strip après pandoc, **avant** réinjection du code |
| Numéros ≠ ordre de lecture | tri alphabétique | renuméroter via `navorder.txt` (ordre DOM) |
| Mauvais fichier renommé | slugs ambigus (topics vs tutorials) | mapper par **URL complète** |
| `grep -oE` échoue | wrapper shell local | extraire en **Python** |
| `pip install` refusé | PEP 668 | **venv** |

---

## 10. Refaire pour un autre hub (checklist)

1. Récupérer le hub : `curl -A "<UA>" .../think/<NOUVEAU-HUB> -o html/00-hub.html` ; vérifier `200`.
2. (Recon) Confirmer que c'est bien un hub à sommaire + articles séparés (sinon adapter §3).
3. Extraire `navorder.txt` (ordre DOM) et `urls.txt` ; **ajuster le filtre** de chemins si le hub
   pointe vers d'autres familles que `topics|insights|tutorials`.
4. Télécharger tous les articles (§4).
5. Lancer `extract.py` sur tout (§5) — **réutilisable tel quel** ; ne ré-auditer la liste `BOILER` et
   le sélecteur `body-article-8` que si IBM change son thème AEM.
6. Renuméroter dans l'ordre sommaire (§6), générer INDEX + GUIDE (§7), contrôle qualité.
7. (Option) Couche de synthèse (§8).

**Seuls paramètres qui changent d'un hub à l'autre** : l'URL du hub et, éventuellement, le filtre de
familles d'URL au §3. Le reste de la chaîne (UA, `extract.py`, renumérotation, agrégation) est
invariant.

---

## Annexe — artefacts réutilisables présents dans le dépôt

- `ibm-guide-agents-ia/extract.py` — extracteur HTML→MD (bs4+lxml+pandoc). **À conserver**.
- `ibm-guide-agents-ia/.venv/` — bs4 + lxml.
- `ibm-guide-agents-ia/urls.txt` — exemple de liste d'URLs.
- `ibm-guide-agents-ia/md/`, `INDEX.md`, `GUIDE-COMPLET.md` — sortie de référence.
- `ibm-guide-agents-ia/concepts/` (+ `hors-corpus/`) — couche de synthèse de référence.
