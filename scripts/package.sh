#!/usr/bin/env bash
# Package a skill directory into dist/<name>.skill (a zip archive).
# Run from the repo root:  ./scripts/package.sh
set -euo pipefail

cd "$(dirname "$0")/.."
mkdir -p dist

for skill_dir in skills/*/; do
    name="$(basename "$skill_dir")"
    out="dist/${name}.skill"
    rm -f "$out"
    ( cd skills && zip -qr "../${out}" "$name" -x '*/__pycache__/*' -x '*.pyc' -x '.DS_Store' )
    echo "packaged ${out} ($(unzip -l "$out" | tail -1 | awk '{print $2}') files, $(du -h "$out" | cut -f1))"
done
