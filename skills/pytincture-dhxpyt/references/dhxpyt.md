# dhxpyt quick reference

Python wrapper around DHTMLX UI widgets, for use inside pytincture/Pyodide apps.
Pytincture 1.0 locks `dhxpyt==0.9.18` as its compatibility release.

## The entrypoint pattern

Subclass `MainWindow` and implement **`load_ui()` only**:

```python
from dhxpyt.layout import MainWindow

class MyApp(MainWindow):
    def load_ui(self):
        self.set_theme("dark")
        self.layout = self.add_layout(layout_config={...})
```

`Layout` uses a `LoadUICaller` metaclass (`dhxpyt/layout/layout.py`) that calls
`load_ui()` automatically once the instance is constructed. **Do not** override
`__init__` to call `load_ui()` yourself — that builds the entire UI twice, and
every widget gets attached to its cell twice:

```python
# Anti-pattern
class MyApp(MainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()      # metaclass already does this
```

Put state that `load_ui` needs at the top of `load_ui`, not in an `__init__`.

## Composition

Build UIs by calling `add_layout` to create cells, then mount widgets into those
cells with the `add_*` helpers. Prefer the helpers over constructing a widget
directly — they mount into a container that already exists:

```python
panel = layout.add_cardpanel(id="tasks_cell", cardpanel_config=panel_config)
```

```python
# Anti-pattern: fails unless that DOM node was already created with attach_html
CardPanel(panel_config, root="#tasks_cardpanel")
```

The `id` passed to any `add_*` helper is an **existing cell id** in the layout or
tabbar you are calling it on, not a new name you invent.

The full helper list is in [`dhxpyt/index.md`](dhxpyt/index.md).

## Configuration and events

- Widgets take `*Config` objects or plain dicts.
- Event handlers register through `.on_*` methods: `toolbar.on_click(handler)`.
- Toolbar and sidebar `on_click` handlers receive `(id, event)`.

## Gotchas

- **`SeparatorConfig` is defined in three modules** (`toolbar`, `sidebar`,
  `ribbon`) and they are different classes. Importing more than one unqualified
  silently shadows the others — alias them:
  `from dhxpyt.toolbar import SeparatorConfig as ToolbarSeparatorConfig`.
- **Combo items go in `data`, not `options`.** `ComboConfig` has no `options`
  parameter; passing one raises
  `ComboConfig.__init__() got an unexpected keyword argument 'options'`.
  See [`dhxpyt/form.md`](dhxpyt/form.md).
- **`Tabbar.add_cardpanel` takes `cardpanel_config=`**, not `panel_config=`.
- **`GridConfig(data=...)` wants `List[Dict[str, Any]]`.** A BFF method that
  returns JSON text must be decoded with `json.loads()` first, or the grid
  renders empty.

## API reference

[`dhxpyt/index.md`](dhxpyt/index.md) indexes one page per module, generated from
the dhxpyt source by `scripts/generate_reference.py` in this repo. Load only the
module you need. Regenerate after a widgetset bump:

```bash
python3 scripts/generate_reference.py /path/to/dhx_pytincture_widgetset
```

## Local example

`assets/examples/dhxpyt_ui/testui.py` — minimal layout + toolbar + grid.
