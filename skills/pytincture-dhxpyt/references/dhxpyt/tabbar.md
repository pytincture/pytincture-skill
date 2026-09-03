# dhxpyt.tabbar

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### TabConfig
Configuration class for individual tabs in the Tabbar.

```python
TabConfig(
    id: str,
    tab: str = None,
    tabCss: str = None,
    css: str = None,
    header: str = None,
    html: str = None,
    padding: Union[int, str] = None,
    tabWidth: Union[int, str] = None,
    tabHeight: Union[int, str] = None,
)
```

### TabbarConfig
Configuration class for Tabbar.

```python
TabbarConfig(
    views: List[TabConfig],
    activeTab: str = None,
    closable: Union[bool, List[str]] = None,
    css: str = None,
    disabled: Union[str, List[str]] = None,
    mode: str = None,
    noContent: bool = None,
    tabAlign: str = None,
    tabAutoHeight: bool = None,
    tabAutoWidth: bool = None,
    tabHeight: Union[int, str] = None,
    tabWidth: Union[int, str] = None,
)
```

## Widget classes

### Tabbar

```python
add_grid(id: str = 'mainwindow', grid_config: GridConfig = None) -> Grid
add_cardflow(id: str, cardflow_config: CardFlowConfig = None) -> Any
add_cardpanel(id: str, cardpanel_config: CardPanelConfig = None) -> CardPanel
wait_for_element(selector, callback)
add_kanban(id: str = 'mainwindow', kanban_config: KanbanConfig = None, kanban_callback: callable = None) -> None
create_kanban()
add_menu(id: str = 'mainwindow_header', menu_config: MenuConfig = None) -> Menu
add_toolbar(id: str = 'mainwindow', toolbar_config: ToolbarConfig = None) -> Toolbar
add_sidebar(id: str, sidebar_config: SidebarConfig = None) -> Sidebar
add_form(id: str, form_config: FormConfig = None) -> Form
add_listbox(id: str, listbox_config: ListboxConfig = None) -> Any
add_calendar(id: str, calendar_config: CalendarConfig = None) -> Any
add_chart(id: str, chart_config: ChartConfig = None) -> Any
add_pagination(id: str, pagination_config: PaginationConfig = None) -> Any
add_ribbon(id: str, ribbon_config: RibbonConfig = None) -> Any
add_tabbar(id: str, tabbar_config: TabbarConfig = None) -> Any
add_timepicker(id: str, timepicker_config: TimepickerConfig = None) -> Any
add_tree(id: str, tree_config: TreeConfig = None) -> Any
add_tab(config: Dict[str, Any], index: int) -> None
destructor() -> None
disable_tab(id: str) -> bool
enable_tab(id: str) -> None
get_active() -> str
get_cell(id: str) -> Any
get_id(index: int) -> str
get_widget() -> Any
is_disabled(id: str) -> bool
paint() -> None
remove_tab(id: str) -> None
set_active(id: str) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_close(handler: Callable[[str], None]) -> None
on_before_change(handler: Callable[[str, str], Union[bool, None]]) -> None
on_before_close(handler: Callable[[str], Union[bool, None]]) -> None
on_change(handler: Callable[[str, str], None]) -> None
active_tab() -> str
active_tab(value: str) -> None
closable() -> Union[bool, List[str]]
closable(value: Union[bool, List[str]]) -> None
css() -> str
css(value: str) -> None
disabled() -> Union[str, List[str]]
disabled(value: Union[str, List[str]]) -> None
mode() -> str
mode(value: str) -> None
no_content() -> bool
no_content(value: bool) -> None
tab_align() -> str
tab_align(value: str) -> None
tab_auto_height() -> bool
tab_auto_height(value: bool) -> None
tab_auto_width() -> bool
tab_auto_width(value: bool) -> None
tab_height() -> Union[int, str]
tab_height(value: Union[int, str]) -> None
tab_width() -> Union[int, str]
tab_width(value: Union[int, str]) -> None
views() -> List[Dict[str, Any]]
views(value: List[Dict[str, Any]]) -> None
attach(id: str, component: Union[str, Any], config: Dict[str, Any] = None) -> Any
attach_html(id: str, html: str) -> None
get_cell_parent(id: str) -> Any
get_cell_widget(id: str) -> Any
```
