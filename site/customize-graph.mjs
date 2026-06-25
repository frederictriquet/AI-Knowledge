// Colore les nœuds du graphe Quartz par dossier, comme les colorGroups d'Obsidian
// (.obsidian/graph.json). Quartz par défaut ne colore que selon courant/visité/tag.
//
// Appelé par scripts/build-site.sh sur le clone Quartz :
//   node site/customize-graph.mjs <chemin vers graph.inline.ts>
//
// Échoue (exit 1) si le bloc cible n'est plus là → on préfère casser le build
// plutôt que de produire un graphe non patché silencieusement.
import { readFileSync, writeFileSync } from "node:fs"

const file = process.argv[2]
if (!file) {
  console.error("customize-graph: chemin du fichier graph.inline.ts attendu en argument")
  process.exit(1)
}

// Couleurs reprises de .obsidian/graph.json (rgb → hex). Les espaces de dossier
// sont slugifiés par Quartz : « fiches outils/ » → « fiches-outils/ ».
const PREFIX_COLORS = [
  ['fiches-outils/', '#FFA500'], // outils (orange)
  ['MOC/', '#50CA78'], // hubs thématiques (vert)
  ['fiches/', '#4A9CFF'], // concepts (bleu)
]

let src = readFileSync(file, "utf8")

const re =
  /\} else if \(visited\.has\(d\.id\) \|\| d\.id\.startsWith\("tags\/"\)\) \{\s*return computedStyleMap\["--tertiary"\]\s*\} else \{\s*return computedStyleMap\["--gray"\]\s*\}/

if (!re.test(src)) {
  console.error("customize-graph: bloc `color` introuvable — Quartz a-t-il changé ? (build interrompu)")
  process.exit(1)
}

const branches = PREFIX_COLORS.map(
  ([p, c]) => `    } else if (d.id.startsWith("${p}")) {\n      return "${c}"`,
).join("\n")

src = src.replace(
  re,
  `} else if (d.id.startsWith("tags/")) {
      return computedStyleMap["--tertiary"]
${branches}
    } else {
      return computedStyleMap["--gray"]
    }`,
)

// 2. Légende des couleurs, injectée dans le conteneur du graphe (local + global).
const anchor = "graph.appendChild(app.canvas)"
if (!src.includes(anchor)) {
  console.error("customize-graph: ancre `graph.appendChild(app.canvas)` introuvable (build interrompu)")
  process.exit(1)
}

const legend = `graph.appendChild(app.canvas)
  // légende des couleurs par dossier (cf. customize-graph.mjs)
  graph.querySelector(".graph-legend")?.remove()
  const legend = document.createElement("div")
  legend.className = "graph-legend"
  legend.style.cssText = "position:absolute;left:.5rem;bottom:.5rem;display:flex;flex-wrap:wrap;gap:.1rem .6rem;padding:.25rem .5rem;font-size:.7rem;line-height:1.4;color:var(--darkgray);background:var(--light);border:1px solid var(--lightgray);border-radius:4px;pointer-events:none;z-index:5;"
  ;[["#4A9CFF", "concepts"], ["#FFA500", "outils"], ["#50CA78", "MOC"]].forEach(([c, label]) => {
    const item = document.createElement("span")
    item.style.cssText = "display:inline-flex;align-items:center;white-space:nowrap;"
    const dot = document.createElement("i")
    dot.style.cssText = "width:8px;height:8px;border-radius:50%;margin-right:4px;flex:none;background:" + c + ";"
    item.append(dot, document.createTextNode(label))
    legend.appendChild(item)
  })
  graph.appendChild(legend)`

src = src.replace(anchor, legend)

writeFileSync(file, src)
console.log("customize-graph: couleurs + légende de graphe appliquées")
