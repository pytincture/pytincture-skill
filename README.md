# pytincture skills

Agent skills for the [pytincture](https://github.com/pytincture/pytincture)
framework and its widgetsets, [dhxpyt](https://github.com/pytincture/dhx_pytincture_widgetset)
and [wapyt](https://github.com/WAwesome-AI/wa_pytincture_widgetset). Compatible
with Codex / skills.sh.

## Available skills

- **pytincture-dhxpyt** — build or modify pytincture apps: service-mode backends,
  BFF classes and policies, dhxpyt UI layouts, and standalone browser-only pages.
  Tracks pytincture **1.0.0rc5** and dhxpyt **0.9.18**.
- **pytincture-wapyt** — the same for the DHTMLX-free wapyt widgetset: Layout,
  Tree, DataTable, Form, ModalWindow, TabWidget, Sidebar, Chat, Terminal,
  CardPanel, ResourceBoard and filetransfer, plus the wheel and entrypoint
  wiring wapyt apps need. Tracks pytincture **1.0.0rc5** and wapyt **0.1.0**.

## Install

```bash
npx skills add <owner>/<repo>
```

Then reference one in a request, e.g. "use pytincture-dhxpyt to scaffold a dhxpyt UI"
or "use pytincture-wapyt to add a DataTable view".

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
  pytincture-wapyt/
    SKILL.md
    references/
      wapyt/           generated per-module API pages
    assets/
      examples/        runnable service-mode example
scripts/
  generate_reference.py   regenerate references/<package>/ from widgetset source
  package.sh              build dist/*.skill
dist/
  pytincture-dhxpyt.skill
  pytincture-wapyt.skill
```

## Maintenance

Regenerate a widgetset's API reference after it changes, then repackage. The
script detects which package the checkout holds:

```bash
python3 scripts/generate_reference.py /path/to/dhx_pytincture_widgetset
python3 scripts/generate_reference.py /path/to/wa_pytincture_widgetset
./scripts/package.sh
```

Each skill carries its own `references/pytincture.md`, because a skill is
installed on its own. The BFF, policy-hook, health-check and environment
sections are shared text: change them in both files.

`dist/*.skill` is committed and must be rebuilt whenever
anything under `skills/` changes, or installs will ship stale content.
