// Colors the Quartz graph nodes by folder, like Obsidian's colorGroups
// (.obsidian/graph.json). By default Quartz colors only by current/visited/tag.
//
// Called by scripts/build-site.sh on the Quartz clone:
//   node site/customize-graph.mjs <path to graph.inline.ts>
//
// Fails (exit 1) if the target block is no longer there → we prefer to break the build
// rather than silently produce an unpatched graph.
import { readFileSync, writeFileSync } from "node:fs"

const file = process.argv[2]
if (!file) {
  console.error("customize-graph: expected the path to graph.inline.ts as argument")
  process.exit(1)
}

// Colors taken from .obsidian/graph.json (rgb → hex). Prefixes match the
// folder slugs Quartz emits for each corpus.
const PREFIX_COLORS = [
  ['tools/', '#FFA500'], // tools (orange)
  ['themes/', '#50CA78'], // thematic hubs (green)
  ['concepts/', '#4A9CFF'], // concepts (blue)
]

let src = readFileSync(file, "utf8")

const re =
  /\} else if \(visited\.has\(d\.id\) \|\| d\.id\.startsWith\("tags\/"\)\) \{\s*return computedStyleMap\["--tertiary"\]\s*\} else \{\s*return computedStyleMap\["--gray"\]\s*\}/

if (!re.test(src)) {
  console.error("customize-graph: `color` block not found — has Quartz changed? (build aborted)")
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

// 2. Color legend, injected into the graph container (local + global).
const anchor = "graph.appendChild(app.canvas)"
if (!src.includes(anchor)) {
  console.error("customize-graph: anchor `graph.appendChild(app.canvas)` not found (build aborted)")
  process.exit(1)
}

const legend = `graph.appendChild(app.canvas)
  // per-folder color legend (cf. customize-graph.mjs)
  graph.querySelector(".graph-legend")?.remove()
  const legend = document.createElement("div")
  legend.className = "graph-legend"
  legend.style.cssText = "position:absolute;left:.5rem;bottom:.5rem;display:flex;flex-wrap:wrap;gap:.1rem .6rem;padding:.25rem .5rem;font-size:.7rem;line-height:1.4;color:var(--darkgray);background:var(--light);border:1px solid var(--lightgray);border-radius:4px;pointer-events:none;z-index:5;"
  ;[["#4A9CFF", "concepts"], ["#FFA500", "tools"], ["#50CA78", "themes"]].forEach(([c, label]) => {
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
console.log("customize-graph: graph colors + legend applied")
