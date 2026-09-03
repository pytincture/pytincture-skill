---
name: pytincture-dhxpyt
description: Build or modify apps that use the pytincture framework and the dhxpyt widgetset. Use when asked to create pytincture services, add backend-for-frontend (BFF) classes/policies, generate UI layouts with dhxpyt widgets (grid, form, toolbar, sidebar, tabbar, etc.), or build standalone browser-only pytincture pages that run Python via Pyodide.
---

# Pytincture + DhxPyt

## Overview

Build Python-driven UIs with dhxpyt and run them either as full pytincture
services or as static browser-only pages. Targets pytincture **1.0.0rc5** and
dhxpyt **0.9.18** (the release pytincture 1.0 locks). Service mode needs Python
3.13 or 3.14.

## Pick a mode

- **Service mode** — backend routes, BFF calls, auth, private server Python.
- **Standalone mode** — one static HTML page, no server. No BFF, no auth, and
  everything on the page is visible to the user.

## Rules that apply to every task

1. **Implement `load_ui()` only.** Never override `__init__` to call it —
   dhxpyt's `LoadUICaller` metaclass already calls `load_ui()` after
   construction, so doing both builds the entire UI twice.
2. **Mount widgets with the `add_*` helpers** (`layout.add_grid`,
   `tabbar.add_form`, `layout.add_cardpanel`, …) rather than constructing
   widgets directly. The `id` you pass is an **existing cell id**, not a new
   name. Bare `CardPanel(config, root="#x")` fails unless `#x` already exists.
3. **Alias same-named configs across modules.** `SeparatorConfig` exists in
   `toolbar`, `sidebar` and `ribbon` and they are different classes; importing
   two unqualified silently shadows one.

## Task 1: Service-mode app

1. Write the browser entrypoint: a module whose top-level class subclasses
   `MainWindow` and implements `load_ui()`.
2. Add `widget.py` with literal `__widgetset__` / `__version__`, and
   `import widget` from the entrypoint — the backend discovers the widgetset by
   walking the entrypoint's imports.
3. Add BFF data classes with `@backend_for_frontend`, plus `@bff_policy`,
   `@bff_http_methods` or `@bff_stream` as needed. Call them from the browser
   through the awaitable `name_async()` companion — the plain `name()` form is
   a blocking XHR, deprecated through 1.x.
4. Create the ASGI app with `create_app(PytinctureConfig(...))` in a separate
   `service.py`, and run it with uvicorn. (`launch_service()` still works and is
   the compatibility path for existing code.)
5. Register a policy hook if any export uses `@bff_policy` — without one the
   service **fails closed at startup**. Pytincture enforces declared claims
   itself before the hook; `roles` requires **all** of them and needs an
   identity source, so declaring `roles` on an export a no-login service must
   serve is an unconditional 403.
6. Open `/{application}`, where `{application}` is the **module filename**
   (`py_ui.py` → `/py_ui`), not the class name.

Start from `assets/examples/pytincture_app/`.
Read [`references/pytincture.md`](references/pytincture.md) for the BFF contract,
policy-hook return values, and configuration.

## Task 2: dhxpyt UI

1. Subclass `MainWindow`; implement `load_ui()`.
2. Build cells with `add_layout`, then mount widgets into those cells with the
   `add_*` helpers.
3. Configure widgets with `*Config` classes or plain dicts.
4. Wire events with `.on_*` methods (`toolbar.on_click(handler)`); toolbar and
   sidebar handlers receive `(id, event)`.

Start from `assets/examples/dhxpyt_ui/testui.py`.
Read [`references/dhxpyt.md`](references/dhxpyt.md) for patterns and gotchas, and
[`references/dhxpyt/index.md`](references/dhxpyt/index.md) for the module index
and the full `add_*` helper table. Load a single module page such as
[`references/dhxpyt/form.md`](references/dhxpyt/form.md) when you need exact
config parameters — do not load them all.

## Task 3: Standalone browser page

1. Copy `assets/standalone/index.html`.
2. Export the verified runtime on the build machine:
   `python -m pytincture.assets ./frontend`.
3. Put your Python in `<script type="text/python">` and set `entrypoint` in
   `window.pytinctureAutoStartConfig`.
4. Pin every `#micropip-libs` entry as `name==version` (or a wheel URL with
   `#sha256=`). Bare names are rejected.
5. Serve over HTTP(S); `file://` does not work.

Read [`references/pytincture-runtime.md`](references/pytincture-runtime.md) for
configuration keys, explicit startup, and the CDN escape hatch.

## Known gotchas

| Symptom | Cause and fix |
|---|---|
| UI renders twice; duplicate toolbars/grids | `__init__` calls `load_ui()` and so does the metaclass. Delete the `__init__`. |
| `ComboConfig.__init__() got an unexpected keyword argument 'options'` | Combo items go in `data=`, not `options=`. |
| `CardPanel: target container not found` | Use `layout.add_cardpanel(id=<existing cell>, ...)`, or create the node first with `attach_html`. |
| `Tabbar.add_cardpanel() got an unexpected keyword argument 'panel_config'` | The parameter is `cardpanel_config=`. |
| Grid renders empty despite data | `GridConfig(data=...)` wants `List[Dict]`; `json.loads()` a BFF method that returns JSON text. |
| `DeprecationWarning` from a BFF call | Use the `name_async()` companion and `await` it from a coroutine scheduled with `asyncio.ensure_future()`. |
| Wrong separator style in a toolbar | `sidebar.SeparatorConfig` shadowed `toolbar.SeparatorConfig`. Alias the imports. |
| 404 for `dhxpyt-99.99.99-py3-none-any.whl` | The runtime fell through to `devWheelVersion`. Pin `widgetlib: "dhxpyt==0.9.18"`. |
| micropip install rejected | Every entry needs an exact `name==version` pin or `url#sha256=`. |
| Service refuses to start, mentions `@bff_policy` | Register `set_bff_policy_hook()` or set `BFF_POLICY_HOOK_PATH`. |
| Policy hook raises `RuntimeError` | Hooks must return `True`/`False`/`None`, nothing else. |
| Shell renders but every BFF call answers 403 | An export declares `roles` while no identity source supplies role claims. Drop the requirement, or configure login (`AUTH_USER_CLAIMS`, an authenticator, or an IdP). |

## Resources

### references/
- `pytincture.md` — service mode, BFF contract, policy hooks, config
- `pytincture-runtime.md` — standalone runtime setup and configuration keys
- `dhxpyt.md` — dhxpyt patterns, entrypoint rule, gotchas
- `dhxpyt/index.md` — module index and the `add_*` helper table
- `dhxpyt/<module>.md` — generated per-module config and widget signatures
- `examples.md` — index of bundled example assets

### assets/
- `examples/pytincture_app/` — full service-mode app
- `examples/dhxpyt_ui/` — minimal dhxpyt UI
- `standalone/index.html` — browser-only page template
