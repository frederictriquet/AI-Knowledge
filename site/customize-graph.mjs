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

writeFileSync(file, src)
console.log("customize-graph: couleurs de graphe par dossier appliquées")
