# pytincture skills

Agent skills for the [pytincture](https://github.com/pytincture/pytincture)
framework and the [dhxpyt](https://github.com/pytincture/dhx_pytincture_widgetset)
widgetset. Compatible with Codex / skills.sh.

## Available skills

- **pytincture-dhxpyt** — build or modify pytincture apps: service-mode backends,
  BFF classes and policies, dhxpyt UI layouts, and standalone browser-only pages.

Tracks pytincture **1.0.0rc5** and dhxpyt **0.9.18**.

## Install

```bash
npx skills add <owner>/<repo>
```

Then reference it in a request, e.g. "use pytincture-dhxpyt to scaffold a dhxpyt UI".

## Repo layout

```
skills/
  pytincture-dhxpyt/
    SKILL.md
    references/
      dhxpyt/          generated per-module API pages
    assets/
      examples/        runnable service-mode and UI examples
      standalone/      browser-only page template
scripts/
  generate_reference.py   regenerate references/dhxpyt/ from widgetset source
  package.sh              build dist/*.skill
dist/
  pytincture-dhxpyt.skill
```

## Maintenance

Regenerate the dhxpyt API reference after a widgetset bump, then repackage:

```bash
python3 scripts/generate_reference.py /path/to/dhx_pytincture_widgetset
./scripts/package.sh
```

`dist/pytincture-dhxpyt.skill` is committed and must be rebuilt whenever
anything under `skills/` changes, or installs will ship stale content.
