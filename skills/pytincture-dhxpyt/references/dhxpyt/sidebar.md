# dhxpyt.sidebar

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### ControlConfig

_No keyword parameters._

### CustomHTMLConfig

```python
CustomHTMLConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    html: Optional[str] = None,
    css: Optional[str] = None,
    hidden: Optional[bool] = None,
)
```

### MenuItemConfig

```python
MenuItemConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    value: Optional[str] = None,
    items: Optional[List['ControlConfig']] = None,
    count: Optional[int] = None,
    countColor: Optional[str] = None,
    hotkey: Optional[str] = None,
    html: Optional[str] = None,
    icon: Optional[str] = None,
    tooltip: Optional[str] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    hidden: Optional[bool] = None,
)
```

### NavItemConfig

```python
NavItemConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    value: Optional[str] = None,
    items: Optional[List['ControlConfig']] = None,
    active: Optional[bool] = None,
    count: Optional[int] = None,
    countColor: Optional[str] = None,
    group: Optional[str] = None,
    hotkey: Optional[str] = None,
    html: Optional[str] = None,
    icon: Optional[str] = None,
    tooltip: Optional[str] = None,
    twoState: Optional[bool] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    hidden: Optional[bool] = None,
)
```

### SeparatorConfig

```python
SeparatorConfig(
    id: Optional[str] = None,
)
```

### SidebarConfig
Configuration class for the Sidebar widget.

```python
SidebarConfig(
    data: Optional[List[ControlConfig]] = None,
    collapsed: Optional[bool] = None,
    css: Optional[str] = None,
    menuCss: Optional[str] = None,
    minWidth: Union[int, str] = None,
    width: Union[int, str] = None,
)
```

### SpacerConfig

```python
SpacerConfig(
    id: Optional[str] = None,
)
```

### TitleConfig

```python
TitleConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    value: Optional[str] = None,
    html: Optional[str] = None,
    tooltip: Optional[str] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    hidden: Optional[bool] = None,
)
```

## Widget classes

### Sidebar

```python
collapse() -> None
destructor() -> None
disable(ids: Union[str, int, List[Union[str, int]]] = None) -> None
enable(ids: Union[str, int, List[Union[str, int]]] = None) -> None
expand() -> None
get_selected() -> List[Union[str, int]]
hide(ids: Union[str, int, List[Union[str, int]]] = None) -> None
is_collapsed() -> bool
is_disabled(id: Union[str, int]) -> bool
is_selected(id: Union[str, int]) -> bool
paint() -> None
select(id: Union[str, int], unselect: bool = True) -> None
show(ids: Union[str, int, List[Union[str, int]]] = None) -> None
toggle() -> None
unselect(id: Union[str, int] = None) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_collapse(handler: Callable[[], None]) -> None
on_after_expand(handler: Callable[[], None]) -> None
on_after_hide(handler: Callable[[Any], None]) -> None
on_before_collapse(handler: Callable[[], Union[bool, None]]) -> None
on_before_expand(handler: Callable[[], Union[bool, None]]) -> None
on_before_hide(handler: Callable[[Union[str, int], Any], Union[bool, None]]) -> None
on_click(handler: Callable[[Union[str, int], Any], None]) -> None
on_input_blur(handler: Callable[[Union[str, int]], None]) -> None
on_input_created(handler: Callable[[Union[str, int], Any], None]) -> None
on_input_focus(handler: Callable[[Union[str, int]], None]) -> None
on_keydown(handler: Callable[[Any, Optional[str]], None]) -> None
on_open_menu(handler: Callable[[Union[str, int]], None]) -> None
```
