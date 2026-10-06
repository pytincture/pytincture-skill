---
name: pytincture-wapyt
description: Build or modify pytincture apps that use the wapyt widgetset (wA PyTincture, the DHTMLX-free widgets) — Layout/MainWindow, Toolbar, ContextMenu, ProgressBar, Tree, DataTable, Form, ModalWindow, TabWidget, Sidebar, Chat, Terminal, CardPanel, ResourceBoard, the message toasts/dialogs and the filetransfer helpers. Use when code imports `wapyt`, when asked for a pytincture UI without DHTMLX/dhxpyt, or when wiring a wapyt app's service.py, BFF classes, browser wheel or APP_ENTRYPOINT.
---

# Pytincture + wapyt

## Overview

wapyt declares widgets in Python and renders them as plain DOM through its
bundled JS, inside Pyodide. Every widget follows one path: a `*Config`
dataclass → `.to_dict()` (camelCase) → `js.wapyt.<Widget>.new(root, payload)`;
events come back through `.on_*` handlers. Targets pytincture **1.0.0rc5** and
wapyt **0.1.0**. Service mode needs Python 3.13 or 3.14.

wapyt is not dhxpyt. The widget set, names and signatures differ (`TabWidget`
not `Tabbar`, `DataTable` not `Grid`, no menu bar or Chart), so do not carry
dhxpyt code across — look the API up in `references/wapyt/`.

## Rules that apply to every task

1. **Implement `load_ui()` only.** Never define `__init__` to call it — the
   `LoadUICaller` metaclass already calls `load_ui()` after construction, so
   doing both builds the UI twice.
2. **Declare the entrypoint.** pytincture's MainWindow detection only knows
   dhxpyt's class. Put `APP_ENTRYPOINT = "ClassName"` at module level, or name
   the class after the module file. Otherwise the page answers HTTP 422.
3. **Ship the browser wheel.** wapyt is not on PyPI and not in pytincture's
   wheel locks. Build it into the modules folder with wapyt's
   `scripts/dev_wheel.sh <modules_path>` and re-run it after any wapyt change.
4. **Mount widgets with the `Layout.add_*` helpers** into **existing cell
   ids**. Inside a tab, a modal or any other element, construct the widget
   with `container=` (`Form(cfg, container=modal.body)`,
   `DataTable(cfg, container=tabs.get_cell("files"))`).
5. **BFF calls are `await X().name_async(...)`**, scheduled from sync handlers
   with `asyncio.ensure_future` and wrapped so exceptions are logged. Never
   `asyncio.run` — it breaks Pyodide's event loop for the session.

## Task 1: Service-mode app

1. Write the browser entrypoint: a `MainWindow` subclass that implements
   `load_ui()`, plus `APP_ENTRYPOINT`.
2. Add `widget.py` with literal `__widgetset__ = "wapyt"` and
   `__version__ = "0.1.0"`, and `import widget` from the entrypoint.
3. Build the wheel into the folder: `.../wa_pytincture_widgetset/scripts/dev_wheel.sh .`
4. Add BFF classes with `@backend_for_frontend`. Keep state in storage, never
   in BFF module globals — the module is re-executed for every call.
5. Create the ASGI app with `create_app(PytinctureConfig(...))` in `service.py`.
   If any export carries `@bff_policy`, register the hook by **dotted path**:
   `environment={"BFF_POLICY_HOOK_PATH": "service.policy_hook"}`.
   `set_bff_policy_hook()` does not reach a `create_app()` app.
6. Run `python -m uvicorn service:app --port 8070` and open
   `/{module filename}`.

Start from `assets/examples/wapyt_app/`.
Read [`references/pytincture.md`](references/pytincture.md) for the BFF
contract, policy hooks, wheel resolution and configuration.

## Task 2: wapyt UI

1. Give the `MainWindow` subclass a class-level `layout_config =
   LayoutConfig(rows=[...])` of `CellConfig`s. Without one you get the default
   `mainwindow_header` + `mainwindow` cells.
2. Mount widgets into those cells with `add_toolbar` (header row),
   `add_tree`, `add_datatable`, `add_form`, `add_tabwidget`, … or put HTML in
   one with `attach_html`. Build toolbars with `Toolbar`, not HTML strings.
3. Wire events with `.on_*`; most handlers receive one dict payload.
4. Load data in an async method scheduled from `load_ui()`, then push it in
   with `set_rows` / `set_items` / `set_values`.

Read [`references/wapyt.md`](references/wapyt.md) for composition, sizing,
events, icons, theming and escaping rules, and
[`references/wapyt/index.md`](references/wapyt/index.md) for the module index
and `add_*` helpers. Load a single module page such as
[`references/wapyt/datatable.md`](references/wapyt/datatable.md) when you need
exact config fields — do not load them all.

## Known gotchas

| Symptom | Cause and fix |
|---|---|
| HTTP 422 opening the app | No entrypoint found. Add `APP_ENTRYPOINT = "ClassName"`. |
| Page loads but no widgets / widgetset 404 | No wapyt wheel in `modules_path`, or a stale one. Re-run `dev_wheel.sh`, restart. |
| Widgetset discovery finds nothing with `from wapyt import ...` | wapyt installed **editable** server-side. Add `widget.py` + `import widget`, or install non-editable. |
| UI renders twice | `__init__` calls `load_ui()` and so does the metaclass. Delete the `__init__`. |
| Service refuses to start, mentions `@bff_policy` | Hook registered with `set_bff_policy_hook()` under `create_app()`. Use `BFF_POLICY_HOOK_PATH`. |
| Data written by a BFF call is gone on the next call | State kept in a BFF module global; the module re-executes per call. Use storage. |
| `CellConfig(width=...)` ignored / pane squeezed | Use `"100%"` for fill-the-rest, `"auto"` for content size, `"220px"` for fixed. |
| Modal buttons clipped below the fold | `ModalConfig(height=...)` is honest; body content scrolls inside it. Make it taller. |
| Hidden modals pile up in the DOM | `hide()` keeps the overlay. Use `ModalConfig(dispose_on_close=True)` and `close()` for per-use dialogs. |
| Form vanished after `set_content` | `set_content` replaces the body. Mount into `modal.body` instead. |
| A `body { font-family }` rule doesn't change the UI | Layouts and modals read `--wapyt-font-family`. Override that on `:root`. |
| Button text overlapping / icons show as words | A ligature icon font. Use MDI classes (`mdi-pencil`); never add a Material Icons/Symbols `<link>`. |
| `if el is None:` never fires on a DOM lookup | Your own JS calls (`js.document.getElementById`) return JS `null` as `JsNull`, not `None`. Test truthiness. wapyt payloads and getters already give `None`. |
| Exception in an async handler vanishes | `ensure_future` swallows it. Wrap the coroutine and `js.console.error(traceback.format_exc())`. |
| Chat history lost on reload | `ChatConfig(storage_key=...)` unset; without it the prefix is random per instance. |
| Stream renders an empty message | Backend sent an in-band `{"error": ...}` chunk. Use `Chat.consume_stream`, or check `Chat.extract_stream_error`. |
| Drawing a progress bar from divs and widths | `ProgressBar` (live: `set_value(v, max, text=)`, `set_state`) or `progress_html(...)` for string-built markup. |
| Building a right-click menu from HTML | Use `ContextMenu`: `attach(selector)` plus `data-context` on rows, or `show_at(x, y, hide=[...], disable=[...])` per opening. |
| Reaching for `window.confirm()` or a hand-made toast | Use `wapyt.message`: `toast(...)`, and `await message.confirm(...)` / `alert` / `prompt` from an async handler. |
| File picker raises `SecurityError` | A `filetransfer.pick_*` call ran after an `await`. Call it first in the click handler. |
| Mic button does nothing | pytincture sends `Permissions-Policy: microphone=()`. Set `PYTINCTURE_ALLOW_MICROPHONE=1` and serve a secure context. |

## Resources

### references/
- `pytincture.md` — service mode, wheel resolution, BFF contract, policy hooks
- `wapyt.md` — composition, sizing, events, icons, theming, escaping, per-widget notes
- `wapyt/index.md` — module index and the `add_*` helper table
- `wapyt/<module>.md` — generated per-module config fields and widget methods
- `examples.md` — what the bundled example demonstrates

### assets/
- `examples/wapyt_app/` — service-mode app: Tree + DataTable + Form in a modal, fed by a BFF
