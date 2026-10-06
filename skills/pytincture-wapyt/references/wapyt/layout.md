# wapyt.layout

Generated from wapyt 0.1.0 source by `scripts/generate_reference.py`.

## Config and data classes

### CellConfig
Declarative configuration for a single layout cell.

```python
CellConfig(
    id: Optional[str] = None,
    header: Optional[str] = None,
    width: Optional[Size] = None,
    height: Optional[Size] = None,
    css: Optional[str] = None,
    collapsible: bool = False,
    collapsed: bool = False,
    hidden: bool = False,
    html: Optional[str] = None,
    rows: Optional[Sequence['CellConfig']] = None,
    cols: Optional[Sequence['CellConfig']] = None,
    grow: Optional[float] = None,
    shrink: Optional[float] = None,
    min_size: Optional[Size] = None,
)
```

### LayoutConfig
Top-level layout definition supporting nested rows/columns.

```python
LayoutConfig(
    type: str = 'line',
    rows: Optional[Sequence[CellConfig]] = field(default=None),
    cols: Optional[Sequence[CellConfig]] = field(default=None),
    css: Optional[str] = None,
    gap: Optional[Size] = None,
    borderless: bool = False,
)
```

## Widget classes

### Layout
DOM-driven layout wrapper that mirrors PyTincture's legacy API.

Quick start::

    layout = Layout(LayoutConfig(rows=[CellConfig(id="main", grow=1)]))
    chat = layout.add_chat("main")
    layout.attach_html("main", "<h1>Hydrated</h1>")

`MainWindow` simply instantiates `Layout(mainwindow=True)` so existing
PyTincture apps can continue exposing a `MainWindow` subclass with a
`load_ui` method.

```python
Layout(config: Optional[Union[LayoutConfig, Dict[str, Any]]] = None, *, mainwindow: bool = False, **kwargs)
```

```python
load_ui(*_, **__) -> None
add_layout(id: str = 'mainwindow', layout_config: Optional[LayoutConfig] = None) -> TLayout
add_chat(id: str = 'mainwindow', chat_config: Optional['ChatConfig'] = None) -> 'Chat'
add_cardpanel(id: str = 'mainwindow', cardpanel_config: Optional['CardPanelConfig'] = None) -> 'CardPanel'
add_tabwidget(id: str = 'mainwindow', tab_config: Optional['TabWidgetConfig'] = None) -> 'TabWidget'
add_tree(id: str = 'mainwindow', tree_config: Optional['TreeConfig'] = None) -> 'Tree'
add_datatable(id: str = 'mainwindow', datatable_config: Optional['DataTableConfig'] = None) -> 'DataTable'
add_form(id: str = 'mainwindow', form_config: Optional['FormConfig'] = None) -> 'Form'
add_terminal(id: str = 'mainwindow', terminal_config: Optional['TerminalConfig'] = None) -> 'Terminal'
add_sidebar(id: str = 'mainwindow', sidebar_config: Optional['SidebarConfig'] = None) -> 'Sidebar'
add_resourceboard(id: str = 'mainwindow', resourceboard_config: Optional['ResourceBoardConfig'] = None) -> 'ResourceBoard'
attach_html(id: str, html: str) -> None
attach(id: str, component: Any, config: Optional[Dict[str, Any]] = None) -> Any
destructor() -> None
for_each(callback: Callable[[Any, int, Any], Any]) -> None
get_cell(id: str) -> Any
progress_show(id: Optional[str] = None, text: Optional[str] = None) -> None
progress_hide(id: Optional[str] = None) -> None
remove_cell(id: str) -> None
resize(id: Optional[str] = None) -> None
add_event_handler(event_name: str, handler: Callable) -> None
after_add(handler: Callable) -> None
after_remove(handler: Callable) -> None
after_show(handler: Callable) -> None
after_hide(handler: Callable) -> None
before_remove(handler: Callable) -> None
collapse(id: str) -> None
expand(id: str) -> None
toggle(id: str) -> None
detach(id: str) -> None
hide(id: str) -> None
show(id: str) -> None
is_visible(id: str) -> bool
get_parent(id: str) -> Any
get_widget(id: str) -> Any
attach_html_cell(id: str, html: str) -> None
wait_for_element(selector: str, callback: Callable[[], Any], interval_ms: int = 100) -> None
```

### LoadUICaller


### MainWindow
Legacy-compatible wrapper so existing apps can inherit from `MainWindow`.

```python
set_theme(theme: str) -> None
show_cookie_banner() -> None
hide_cookie_banner() -> None
accept_cookies(_event = None) -> None
reject_cookies(_event = None) -> None
check_cookie_consent() -> None
```
