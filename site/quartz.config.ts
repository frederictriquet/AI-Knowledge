import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Config Quartz du corpus IA.
 *
 * Ce fichier est copié à la racine du clone Quartz par `scripts/build-site.sh`
 * (d'où les imports `./quartz/...`). Il n'est jamais exécuté depuis ce dépôt.
 *
 * `baseUrl` est injecté à la volée via `process.env.BASE_URL` (passé par la CI :
 * `CI_PAGES_URL` côté GitLab, `base_url` d'actions/configure-pages côté GitHub).
 * Quartz attend un host SANS schéma ni slash final → on nettoie la valeur.
 */
const baseUrl = (process.env.BASE_URL ?? "localhost:8080")
  .replace(/^https?:\/\//, "")
  .replace(/\/+$/, "")

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Corpus IA — Knowledge Base",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "fr-FR",
    baseUrl,
    // Exclut l'outillage et les sources brutes : on ne publie que le wiki.
    ignorePatterns: [
      "private",
      "templates",
      ".obsidian",
      ".git",
      ".git/**",
      ".github",
      "tools",
      "tools/**",
      "sources",
      "sources/**",
      "scripts",
      "site",
      "node_modules",
      "node_modules/**",
      "public",
      "**/*.py",
      "*.base",
      "scratchpad_reddit.*",
      // Docs internes / de travail / générées — hors site public (choix de curation).
      "CLAUDE.md",
      "log.md",
      "outils candidats.md",
      "RAPPORT-CORPUS.md",
      "process",
      "process/**",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: { light: "github-light", dark: "github-dark" },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      // "relative" : nos liens internes sont des liens markdown relatifs
      // (`[X](slug.md)`, `../fiches/...`) depuis la passe OKF, pas des wikilinks.
      Plugin.CrawlLinks({ markdownLinkResolution: "relative" }),
      Plugin.Description(),
      // Pas de Plugin.Latex : le corpus n'a pas de maths, et KaTeX capturerait
      // les prix en « 49 $/mois » (paires de `$`) en les rendant en charabia.
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: true }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // CustomOgImages désactivé (build plus rapide ; à réactiver si besoin de cartes OG).
    ],
  },
}

export default config
