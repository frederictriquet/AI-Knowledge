#!/usr/bin/env bash
#
# Construit le vault Obsidian en site statique Quartz dans ./public.
#
# SOURCE UNIQUE de la logique de build : les deux CI (GitHub Actions et GitLab CI)
# ne font qu'appeler ce script. Elles ne diffèrent que par la plomberie propre à
# chaque plateforme et par la provenance de BASE_URL.
#
# Entrées (variables d'environnement) :
#   BASE_URL    URL publique du site (avec ou sans schéma). Nécessaire pour des
#               liens absolus, le RSS et le sitemap corrects.
#               - GitLab : $CI_PAGES_URL
#               - GitHub : sortie `base_url` d'actions/configure-pages
#   QUARTZ_REF  Ref git de Quartz à utiliser (défaut : v4).
#
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"   # racine du dépôt = contenu
QUARTZ_REF="${QUARTZ_REF:-v4}"
BUILD_DIR="$(mktemp -d)"
trap 'rm -rf "$BUILD_DIR"' EXIT

echo "▶ contenu=$REPO"
echo "▶ quartz=$QUARTZ_REF  baseUrl=${BASE_URL:-<non défini, fallback localhost>}"

git clone --depth 1 --branch "$QUARTZ_REF" \
  https://github.com/jackyzha0/quartz "$BUILD_DIR/quartz"

# Notre config remplace celle par défaut du clone (imports ./quartz/... résolus ici).
cp "$REPO/site/quartz.config.ts" "$BUILD_DIR/quartz/quartz.config.ts"

# Colore le graphe par dossier (couleurs des colorGroups Obsidian).
node "$REPO/site/customize-graph.mjs" \
  "$BUILD_DIR/quartz/quartz/components/scripts/graph.inline.ts"

cd "$BUILD_DIR/quartz"
npm install --no-audit --no-fund

# -d : contenu = la racine du dépôt (filtrée par ignorePatterns dans la config)
# -o : sortie dans ./public du dépôt (ramassée comme artefact par la CI)
npx quartz build --directory "$REPO" --output "$REPO/public"

echo "✔ site généré → $REPO/public"
