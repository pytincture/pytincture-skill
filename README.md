# pytincture skills

This repo contains Codex/skills.sh-compatible agent skills.

## Available skills

- **pytincture-dhxpyt**: Build or modify apps that use the pytincture framework and the dhxpyt widgetset. Supports full backend services, BFF policies, dhxpyt UI layouts, and standalone browser-only pytincture.js usage.

## Install

With the skills CLI:

```bash
npx skills add <owner>/<repo>
```

After installing, use the skill in Codex by referencing it directly in a request (e.g., "use pytincture-dhxpyt to scaffold a dhxpyt UI").

## Repo layout

```
skills/
  pytincture-dhxpyt/
    SKILL.md
    references/
    assets/
```

## Notes

A packaged artifact is also available at `dist/pytincture-dhxpyt.skill`.
