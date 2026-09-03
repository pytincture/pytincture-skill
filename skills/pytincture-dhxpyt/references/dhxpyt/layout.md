# dhxpyt.layout

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### CellConfig
Configuration class for individual cells in the Layout.

```python
CellConfig(
    id: str = None,
    header: str = None,
    width: Union[str, int] = None,
    height: Union[str, int] = None,
    css: str = None,
    collapsable: bool = False,
    hidden: bool = False,
)
```

### LayoutConfig
Configuration class for Layout. Contains rows and columns with nested cells.

```python
LayoutConfig(
    type: str = 'line',
    rows: List[List[CellConfig]] = None,
    cols: List[List[CellConfig]] = None,
    css: str = None,
)
```

## Widget classes

### Layout

```python
load_ui(*args, **kwargs)
add_grid(id: str = 'mainwindow', grid_config: GridConfig = None) -> Grid
wait_for_element(selector, callback)
add_kanban(id: str = 'mainwindow', kanban_config: KanbanConfig = None, kanban_callback: callable = None) -> None
create_kanban()
add_layout(id: str = 'mainwindow', layout_config: LayoutConfig = None) -> TLayout
add_menu(id: str = 'mainwindow_header', menu_config: MenuConfig = None) -> Menu
add_toolbar(id: str = 'mainwindow', toolbar_config: ToolbarConfig = None) -> Toolbar
add_sidebar(id: str, sidebar_config: SidebarConfig = None) -> Sidebar
add_form(id: str, form_config: FormConfig = None) -> Form
add_listbox(id: str, listbox_config: ListboxConfig = None) -> Any
add_calendar(id: str, calendar_config: CalendarConfig = None) -> Any
add_chart(id: str, chart_config: ChartConfig = None) -> Any
add_pagination(id: str, pagination_config: PaginationConfig = None) -> Any
add_cardflow(id: str, cardflow_config: CardFlowConfig = None) -> Any
add_cardpanel(id: str, cardpanel_config: CardPanelConfig = None) -> CardPanel
add_chat(id: str, chat_config: ChatConfig = None) -> Chat
add_ribbon(id: str, ribbon_config: RibbonConfig = None) -> Any
add_tabbar(id: str, tabbar_config: TabbarConfig = None) -> Any
add_timepicker(id: str, timepicker_config: TimepickerConfig = None) -> Any
add_tree(id: str, tree_config: TreeConfig = None) -> Any
destructor() -> None
for_each(callback: Callable[[Any, int, List[Any]], Any], parent_id: str = None, level: int = None) -> None
get_cell(id: str) -> Any
progress_hide() -> None
progress_show() -> None
remove_cell(id: str) -> None
resize(id: str) -> None
add_event_handler(event_name: str, handler: Callable) -> None
after_add(handler: Callable) -> None
after_collapse(handler: Callable) -> None
after_expand(handler: Callable) -> None
after_hide(handler: Callable) -> None
after_remove(handler: Callable) -> None
after_resize_end(handler: Callable) -> None
after_show(handler: Callable) -> None
before_add(handler: Callable) -> None
before_collapse(handler: Callable) -> None
before_expand(handler: Callable) -> None
before_hide(handler: Callable) -> None
before_remove(handler: Callable) -> None
before_resize_start(handler: Callable) -> None
before_show(handler: Callable) -> None
cols() -> List[Dict[Any, Any]]
cols(value: List[Dict[Any, Any]]) -> None
css() -> str
css(value: str) -> None
rows() -> List[Dict[Any, Any]]
rows(value: List[Dict[Any, Any]]) -> None
type() -> str
type(value: str) -> None
attach(id: str, component: Union[str, Any], config: Dict[str, Any] = None) -> Any
attach_html(id: str, html: str) -> None
collapse(id: str) -> None
detach(id: str) -> None
expand(id: str) -> None
get_parent(id: str) -> Any
get_widget(id: str) -> Any
hide(id: str) -> None
is_visible(id: str) -> bool
paint() -> None
toggle(id: str) -> None
align() -> str
align(value: str) -> None
resizable() -> bool
resizable(value: bool) -> None
```

### LoadUICaller


### MainWindow

```python
set_theme(theme: str, css_vars = None) -> None
show_cookie_banner()
hide_cookie_banner()
accept_cookies(_event = None)
reject_cookies(_event = None)
check_cookie_consent()
```
