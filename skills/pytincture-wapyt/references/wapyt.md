# wapyt quick reference

wA PyTincture widgetset: DHTMLX-free widgets declared in Python and rendered
as plain DOM by bundled JS inside Pyodide. Targets wapyt **0.1.0**.

Everything is importable from the package root:

```python
from wapyt import (
    MainWindow, Layout, LayoutConfig, CellConfig,
    Tree, TreeConfig, TreeItem, TreeAction,
    DataTable, DataTableConfig, ColumnConfig, TableAction,
    Form, FormConfig, FieldConfig, SelectOption,
    ModalWindow, ModalConfig,
    Toolbar, ToolbarConfig, ToolbarButton, ToolbarText, ToolbarSeparator, ToolbarSpacer,
    TabWidget, TabWidgetConfig, TabConfig,
    Sidebar, SidebarConfig, SidebarItem,
    Chat, ChatConfig, ChatAgentConfig, ChatMessageConfig, ChatStreamError,
    Terminal, TerminalConfig, TerminalTheme,
    CardPanel, CardPanelConfig, CardPanelCardConfig,
    ResourceBoard, ResourceBoardConfig, ResourceItem,
    filetransfer, message,
)
```

## The entrypoint pattern

```python
import widget  # noqa: F401 -- literal __widgetset__/__version__ for the backend
from wapyt import CellConfig, LayoutConfig, MainWindow

APP_ENTRYPOINT = "Dashboard"   # pytincture cannot detect a wapyt MainWindow


class Dashboard(MainWindow):
    layout_config = LayoutConfig(rows=[
        CellConfig(id="header", height="auto"),
        CellConfig(id="body", grow=1, cols=[
            CellConfig(id="nav", width="240px", header="Navigation"),
            CellConfig(id="main", width="100%"),
        ]),
    ])

    def load_ui(self):
        self.set_theme("dark")
        self.tree = self.add_tree("nav", TreeConfig(...))
        self.table = self.add_datatable("main", DataTableConfig(...))
```

`Layout` uses a `LoadUICaller` metaclass that calls `load_ui()` once the
instance is constructed. **Do not** define `__init__` to call it — the UI
builds twice. Put the state `load_ui` needs at the top of `load_ui`.

`MainWindow` mounts into the page's `#maindiv`. A class-level `layout_config`
replaces its default of two rows, `mainwindow_header` (`height="auto"`) and
`mainwindow` (`grow=1`).

## Composition

`Layout.add_*` helpers mount a widget into an **existing cell id** of that
layout and return the widget:

| Helper | Returns |
|---|---|
| `add_layout(id, layout_config)` | nested `Layout` — its helpers take *its* cell ids |
| `add_tree(id, tree_config)` | `Tree` |
| `add_datatable(id, datatable_config)` | `DataTable` |
| `add_form(id, form_config)` | `Form` |
| `add_tabwidget(id, tab_config)` | `TabWidget` |
| `add_toolbar(id="mainwindow_header", toolbar_config)` | `Toolbar` |
| `add_sidebar(id, sidebar_config)` | `Sidebar` |
| `add_chat(id, chat_config)` | `Chat` |
| `add_terminal(id, terminal_config)` | `Terminal` |
| `add_cardpanel(id, cardpanel_config)` | `CardPanel` |
| `add_resourceboard(id, resourceboard_config)` | `ResourceBoard` |
| `attach_html(id, html)` | — raw markup into a cell |

Anywhere that is not a layout cell — a tab, a modal, an element you created —
construct the widget yourself and pass `container=` (a cell or element) or
`root=` (a CSS selector or element id):

```python
tabs = self.add_tabwidget("main", TabWidgetConfig(tabs=[TabConfig(id="files", title="Files")]))
files = DataTable(DataTableConfig(...), container=tabs.get_cell("files"))

modal = ModalWindow(ModalConfig(title="Edit", width=480, height=520, dispose_on_close=True))
form = Form(FormConfig(...), container=modal.body)
modal.show()
```

`ModalWindow.set_content()` **replaces** the body and destroys anything mounted
there; mount into `modal.body` instead.

## Cell sizing

| `width=` / `height=` | Meaning |
|---|---|
| `"100%"` | take the remaining space (`flex: 1 1 0`) |
| `"auto"` | size to content — headers and toolbars |
| `"220px"`, `"30%"`, `220` | fixed basis |
| `grow=1` | flex-grow, for cells without a size |

`min_size` maps to `min-width`/`min-height` along the layout axis. Cells get
`min-width: 0; min-height: 0`, so a wide table or terminal scrolls inside its
cell instead of pushing the layout wider. Cell ops: `collapse`, `expand`,
`toggle`, `hide`, `show`, `progress_show`/`progress_hide`.

## Configuration

- Configs are `@dataclass`es with **snake_case** fields; `to_dict()` emits the
  camelCase payload. Plain dicts are accepted too — then use the JS
  (camelCase) keys.
- **`None` means "omit"** and the JS default wins, so an optional field cannot
  be explicitly cleared to null.
- Most configs have `extra: dict`, merged verbatim into the payload, for JS
  options the dataclass does not model.

## Events

Register with `.on_*(handler)`. Payloads are converted to Python dicts. Most
handlers receive **one dict**:

| Widget | Event → payload |
|---|---|
| `Tree` | `on_select` / `on_activate` (leaf double-click) → `{id, node}`; `on_action` → `{action, id, node}`; `on_toggle` → `{id, expanded}` |
| `Toolbar` | `on_click` → `{id, group, active}` (`group`/`active` are `None` for a plain button) |
| `DataTable` | `on_select` → `{ids, id, rows}`; `on_activate` → `{id, row}`; `on_action` → `{action, id, row, selected}`; `on_columns` → `{reason, column, columns}`; `on_drop` → `{files}` (metadata only) |
| `Form` | `on_submit` → values dict (only after validation passes); `on_change` → `{id, value}`; `on_invalid` → `{errors}`; `on_cancel` |
| `Sidebar` | `on_select` → `{id, data}` |
| `TabWidget` | `on_change` → `{id, viaClick}`; `on_close` → `{id}` |
| `Chat` | `on_send` → `{id, text, message}` (the prompt is `text`); `on_voice` → `{audio, mimeType, bytes, durationMs}` |
| `Terminal` | `on_connect` / `on_disconnect` / `on_title` / ... → dict |

Handlers run synchronously. Anything that awaits a BFF call goes through a
scheduler that logs failures — `asyncio.ensure_future` swallows exceptions:

```python
def spawn(coro, label):
    async def guarded():
        try:
            await coro
        except Exception:
            js.console.error(f"{label} failed:\n{traceback.format_exc()}")
    return asyncio.ensure_future(guarded())

form.on_submit(lambda values: spawn(self.save(values), "save"))
```

**Never `asyncio.run`** in Pyodide: it creates and closes a second loop and
breaks the WebLoop for the rest of the session.

For DOM listeners you add yourself, wrap callbacks with
`pyodide.ffi.create_proxy` and keep a reference to the proxy.

## Pyodide FFI

- JS `null` crosses as **`JsNull`, which is not `None`**, including inside
  most event payloads (Tree's cleared `on_select` `id`; Toolbar maps it to `None`). `if el is None:` never
  fires. Test truthiness: `if not el:`.
- A missing JS property raises `AttributeError` instead of returning
  `undefined`; use `getAttribute()` / `hasattr()` rather than
  `element.dataset.foo`.
- Pass `js.undefined` (not `None`) where a JS API distinguishes "absent".

## Icons

Use **Material Design Icons classes**: `icon="mdi-server"`. pytincture serves
MDI from its own origin. Material Symbols ligature names (`"dashboard"`,
`"settings"`) are mapped onto MDI by `wapyt.icons`. An unmapped name falls back
to a small dot.

**Never add a ligature icon font** (Material Icons/Symbols `<link>`). The CSP
blocks the stylesheet, and the spans then typeset their names as text — the
buttons overlap.

## Theming

- `MainWindow.set_theme("dark")` sets `data-wapyt-theme` on `<html>`; layout,
  tabs, forms, modals and card panels follow it. `Chat` has its own
  `ChatConfig(theme=...)` / `chat.set_theme()`.
- **Typeface: override `--wapyt-font-family`.** Layouts and modals take their
  font from that custom property (a system-UI stack by default), not from
  `body`, so a `body { font-family }` rule does not reach them. Set the
  property once on `:root`:

  ```python
  style = js.document.createElement("style")
  style.textContent = ':root { --wapyt-font-family: "Inter", system-ui, sans-serif; }'
  js.document.head.appendChild(style)
  ```

  Some parts (forms, tables, trees, menus, Chat, CardPanel) still set their
  own `system-ui` stack and ignore the property.

- Colour tokens live in `wapyt.css` as `--wapyt-*` custom properties.

## Escaping (load-bearing)

- `attach_html` and `TabConfig(html=...)` insert **raw HTML**. Escape every
  interpolated value with `html.escape(value, quote=True)`.
- Widget text fields (labels, cell values, titles) are set as text and need no
  escaping.
- `ResourceBoardConfig.detail_template` and CardPanel `card_template` escape
  `{placeholder}` values. A key ending in `Html` (`{modelsHtml}`) opts out —
  use it only for markup you built and escaped yourself.
- Chat renders markdown with its own escaping renderer; artifact previews run in
  `<iframe sandbox="allow-scripts">`. Never add `allow-same-origin`.

## Per-widget notes

### Tree
- Branch vs leaf is decided by having `items`. `on_activate` fires only for
  leaves; a lazily loaded branch needs a placeholder child to show as a branch.
- Use **deterministic node ids**: expansion state is keyed by id and survives
  `set_items()`. Persist it with `get_expanded()` / `set_expanded()`.
- Context menus per node: `TreeAction(scope="leaf"|"branch")`,
  `kinds=[...]` (matches `data["kind"]`), `requires=[...]` (all present in
  `data["flags"]`). Separators between hidden groups hide themselves.

### DataTable
- Sorting and filtering run in the browser on the rows already loaded.
  Pre-format display values in Python and point `ColumnConfig(sort_by=...)` at
  the raw field (`"1.2 MB"` sorted by `size_bytes`).
- Rows need a stable id field (`id_field`, default `"id"`).
- `selection="multi"` adds checkboxes plus ctrl/shift clicks.
- `resizable_columns` / `reorderable_columns` are opt-in; persist layouts from
  `on_columns` and restore with `set_columns` (widths included).
- `ColumnConfig(icon_by="key")` draws a per-cell MDI glyph; `type="icon"`
  renders a whole column of glyphs.
- `set_busy(True)` while loading.

### Form
- Field `type`: `text`, `password`, `email`, `number`, `url`, `textarea`,
  `select`, `checkbox`, `hidden`. Select choices go in `options=` (strings or
  `SelectOption(value, label)`); change them later with `set_field_options`.
- Validation (`required`, `min_length`, `pattern`, `matches`) is client-side
  convenience only. **The BFF revalidates**; show its errors with
  `set_error(field_id, msg)` (`None` = form-wide) or `set_errors({...})`.
- `set_busy(True)` disables the buttons during an async submit.

### ModalWindow
- `ModalConfig(height=...)` is honest: taller content scrolls inside the body.
  Size it for the fields **plus** the button row.
- `hide()` leaves the overlay in the DOM. For a dialog built per use, set
  `dispose_on_close=True` so ×, Escape and a backdrop click remove it, and call
  `close()` yourself on success/cancel.

### TabWidget
- `get_cell(tab_id)` is the container for a widget in that tab.
- `keep_alive=True` (default) keeps hidden tabs mounted. A hidden tab has no
  size, so call e.g. `terminal.fit()` from `on_change` when it becomes visible.

### Chat
- Streaming: `msg_id = chat.start_stream(ChatMessageConfig(role="assistant", content=""))`,
  then `append_stream` / `finish_stream`, or hand a (async) iterator to
  `consume_stream(msg_id, stream)`, which turns in-band `{"error": ...}` chunks
  into `ChatStreamError` instead of an empty message.
- Persistence needs `storage_key=`; without it nothing survives a reload.
- Load the model list from a BFF after construction with `set_extra(...)` /
  `set_models(...)`; `default_model` only covers a first visit.
- `voice_input=True` records and emits audio; transcription is the app's job
  (`set_composer_text`). Needs `PYTINCTURE_ALLOW_MICROPHONE=1` and a secure
  context (`http://127.0.0.1` counts, a LAN IP does not).

### Terminal
- xterm.js is **not bundled**: serve `xterm.js`, `xterm.css`, `addon-fit.js`
  (and optionally `addon-search.js`) yourself under `asset_base` (default
  `/xterm`).
- Bytes never cross into Python — the socket talks to xterm directly. Python
  drives lifecycle only (`connect`, `fit`, `focus`, `destroy`).
- Set `fit_debounce_ms≈120` when the pane can be drag-resized.

### filetransfer
- Not a widget: functions for native pickers and streaming transfers. Bytes
  never cross the FFI.
- Call `pick_save_file` / `pick_folder` / `pick_files` **first** in the click
  handler — the first `await` consumes the user activation and a later picker
  raises `SecurityError`.
- Pickers are Chromium-only. Check `capabilities().pickers` and tell the user
  instead of silently falling back to `download_via_anchor`.

### Toolbar
- Items: `ToolbarButton(id, label, icon, tooltip, variant, toggle, group,
  active, badge, disabled, hidden, show_label, keep_label)`, `ToolbarText(id,
  text)`, `ToolbarSeparator()`, `ToolbarSpacer()`. Ids must be unique.
- `group="mode"` buttons are one-of-several (`get_active("mode")`);
  `toggle=True` latches; `variant` is `primary` / `accent` / `danger`.
- Show and relabel at runtime with `set_hidden`, `set_text`, `set_badge`
  (`None` clears), `set_disabled`, `set_active`.
- `compact="auto"` drops labels to icons when it overflows and restores them
  when it fits; give every button an icon (or `keep_label=True`) so the narrow
  form still makes sense.

### message
- Module functions, not a mounted widget (toasts and dialogs live on `<body>`).
  `message.toast(text, kind="info"|"success"|"warning"|"error", timeout_ms=4000)`;
  `timeout_ms=0` keeps it until dismissed.
- `await message.confirm(text, title=..., ok_text=..., danger=True) -> bool`,
  `await message.alert(...)`, `await message.prompt(text, value=..., password=False) -> str | None`.
  They are coroutines: call them from an async method scheduled with
  `ensure_future`, never in place of a synchronous `window.confirm()` return.
- Text is set as text and `\n\n` starts a paragraph, so pass untrusted strings
  straight in. Cancel, Escape and a backdrop click never confirm; `danger=True`
  starts focus on Cancel.

### CardPanel / ResourceBoard
- `CardPanelConfig` copy is generic by default: empty `title` and
  `description` (an empty description hides its row), "Search…" and "Add".
  Set `add_button_text` and `search_placeholder` to name what the panel
  holds; `searchable=False` hides the search box.
- `CardPanel.register_template(name, factory)` registers a custom card
  renderer; descriptor dicts are the no-JS alternative.

## API reference

[`wapyt/index.md`](wapyt/index.md) indexes one page per module, generated from
the wapyt source by `scripts/generate_reference.py`. Load only the module you
need. Regenerate after a widgetset change:

```bash
python3 scripts/generate_reference.py /path/to/wa_pytincture_widgetset
```
