import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz config of the AI corpus.
 *
 * This file is copied to the root of the Quartz clone by `scripts/build-site.sh`
 * (hence the `./quartz/...` imports). It is never executed from this repository.
 *
 * `baseUrl` is injected on the fly via `process.env.BASE_URL` (passed by the CI:
 * `CI_PAGES_URL` on GitLab, `base_url` of actions/configure-pages on GitHub).
 * Quartz expects a host WITHOUT scheme or trailing slash → we clean the value.
 */
const baseUrl = (process.env.BASE_URL ?? "localhost:8080")
  .replace(/^https?:\/\//, "")
  .replace(/\/+$/, "")

const config: QuartzConfig = {
  configuration: {
    pageTitle: "AI Corpus — Knowledge Base",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl,
    // Excludes the tooling and raw sources: we only publish the wiki.
    ignorePatterns: [
      "private",
      "templates",
      ".obsidian",
      ".git",
      ".git/**",
      ".github",
      "sources",
      "sources/**",
      "scripts",
      "site",
      "node_modules",
      "node_modules/**",
      "public",
      "**/*.py",
      "*.base",
      "**/_*.md",
      "scratchpad_reddit.*",
      // Internal / working / generated docs — outside the public site (curation choice).
      "CLAUDE.md",
      "log.md",
      "tool-candidates.md",
      "corpus-report.md",
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
      // "relative": our internal links are relative markdown links
      // (`[X](slug.md)`, `../concepts/...`) from the OKF pass, not wikilinks.
      Plugin.CrawlLinks({ markdownLinkResolution: "relative" }),
      Plugin.Description(),
      // No Plugin.Latex: the corpus has no math, and KaTeX would capture
      // prices like "$49/month" (pairs of `$`) and render them as gibberish.
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
      // CustomOgImages disabled (faster build; re-enable if OG cards are needed).
    ],
  },
}

export default config
