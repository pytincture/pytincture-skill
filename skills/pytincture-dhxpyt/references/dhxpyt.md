# dhxpyt quick reference

## What it is
- Python wrapper around DHTMLX UI widgets for use inside pytincture/pyodide apps.
- Focus on Python-first UI composition: layout, grid, form, toolbar, sidebar, tabbar, etc.

## Install
```bash
pip install dhxpyt
```

## Docs
See `references/dhxpyt.html` for the API documentation.

## Patterns
- Build UIs by subclassing `MainWindow` and calling `add_layout`, then attach widgets to cells.
- Widgets are configured via `*Config` objects (or dict configs) depending on module.
- Event handlers are usually registered through `.on_*` methods on components (for example, `toolbar.on_click(...)`).

## Combo / Combobox config gotcha
For form combo fields, use `ComboConfig` and pass items via `data`, not `options` (the config does not accept `options`).

See:
- `references/dhxpyt/form.html` for `ComboConfig`
- `references/dhxpyt/combobox.html` for `ComboboxConfig`

## CardPanel docs
If `cardpanel` is missing, regenerate docs from the widgetset repo using the stubbed `generate_docs.sh` script and then update `references/dhxpyt.html` and `references/dhxpyt/cardpanel.html`.

## CardPanel root/container requirement
`CardPanel` needs a real DOM element. Prefer the layout/window helpers (for example, `layout.add_cardpanel(...)`) so the widget is mounted into a valid cell automatically.
If you pass `root="#tasks_cardpanel"` you must create that element first (e.g., with `attach_html`). Alternatively, pass the layout cell directly via `container=...`.

## Local example
`assets/examples/dhxpyt_ui/testui.py` is a minimal layout + toolbar + grid sample.
