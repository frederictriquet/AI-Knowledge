#!/usr/bin/env bash
#
# Builds the Obsidian vault into a Quartz static site in ./public.
#
# SINGLE SOURCE of the build logic: both CIs (GitHub Actions and GitLab CI)
# only call this script. They differ only by the plumbing specific to
# each platform and by the origin of BASE_URL.
#
# Inputs (environment variables):
#   BASE_URL    Public URL of the site (with or without scheme). Required for
#               correct absolute links, RSS and sitemap.
#               - GitLab: $CI_PAGES_URL
#               - GitHub: `base_url` output of actions/configure-pages
#   QUARTZ_REF  Git ref of Quartz to use (default: v4).
#
set -euo pipefail

# Quartz requires Node >= 22 (cf. .nvmrc). Clear failure rather than an opaque EBADENGINE.
NODE_MAJOR="$(node -p 'process.versions.node.split(".")[0]' 2>/dev/null || echo 0)"
if [ "${NODE_MAJOR:-0}" -lt 22 ]; then
  echo "✖ Node >= 22 required (detected: $(node -v 2>/dev/null || echo none)). Try: nvm use" >&2
  exit 1
fi

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"   # repository root
CONTENT="$REPO/wiki"                                      # the corpus = published content
QUARTZ_REF="${QUARTZ_REF:-v4}"
BUILD_DIR="$(mktemp -d)"
trap 'rm -rf "$BUILD_DIR"' EXIT

echo "▶ content=$CONTENT"
echo "▶ quartz=$QUARTZ_REF  baseUrl=${BASE_URL:-<unset, fallback localhost>}"

# Fail fast on broken internal links (Quartz only warns, never fails). Needs
# python3 (stdlib only); skip loudly where it is absent (e.g. the node:22 image).
if command -v python3 >/dev/null 2>&1; then
  echo "▶ checking internal links"
  python3 "$REPO/tools/kb_check_links.py"
else
  echo "⚠ python3 not found — internal link check SKIPPED (run /kb:lint locally)" >&2
fi

git clone --depth 1 --branch "$QUARTZ_REF" \
  https://github.com/jackyzha0/quartz "$BUILD_DIR/quartz"

# Our config replaces the clone's default one (./quartz/... imports resolved here).
cp "$REPO/site/quartz.config.ts" "$BUILD_DIR/quartz/quartz.config.ts"

# Colors the graph by folder (colors of the Obsidian colorGroups).
node "$REPO/site/customize-graph.mjs" \
  "$BUILD_DIR/quartz/quartz/components/scripts/graph.inline.ts"

cd "$BUILD_DIR/quartz"
npm install --no-audit --no-fund

# -d: content = the wiki/ subfolder (corpus only; filtered by ignorePatterns)
# -o: output to the repository's ./public (picked up as an artifact by the CI)
npx quartz build --directory "$CONTENT" --output "$REPO/public"

echo "✔ site generated → $REPO/public"
