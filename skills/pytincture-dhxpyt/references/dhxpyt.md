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

## Local example
`assets/examples/dhxpyt_ui/testui.py` is a minimal layout + toolbar + grid sample.
