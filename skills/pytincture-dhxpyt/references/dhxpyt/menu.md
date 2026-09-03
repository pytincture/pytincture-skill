# dhxpyt.menu

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### MenuConfig
Configuration class for Menu.

```python
MenuConfig(
    css: str = None,
    data: List[MenuItemConfig] = None,
    menuCss: str = None,
    navigationType: str = 'pointer',
)
```

### MenuItemConfig
Configuration class for individual items in the Menu.

```python
MenuItemConfig(
    id: Union[str, int] = None,
    value: str = None,
    type: str = 'menuItem',
    parent: Union[str, int] = None,
    items: List['MenuItemConfig'] = None,
    count: Union[int, str] = None,
    countColor: str = 'danger',
    hotkey: str = None,
    html: str = None,
    icon: str = None,
    css: str = None,
    disabled: bool = False,
    hidden: bool = False,
)
```

## Widget classes

### Menu

```python
destructor() -> None
disable(ids: Union[str, int, List[Union[str, int]]] = None) -> None
enable(ids: Union[str, int, List[Union[str, int]]] = None) -> None
get_selected() -> List[Union[str, int]]
hide(ids: Union[str, int, List[Union[str, int]]] = None) -> None
is_disabled(id: Union[str, int]) -> bool
is_selected(id: Union[str, int]) -> bool
paint() -> None
select(id: Union[str, int], unselect: bool = True) -> None
show(ids: Union[str, int, List[Union[str, int]]] = None) -> None
show_at(elem: Union[str, Any], show_at: str = 'bottom') -> None
unselect(id: Union[str, int] = None) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_hide(handler: Callable[[Any], None]) -> None
on_before_hide(handler: Callable[[Union[str, int], Any], Union[bool, None]]) -> None
on_click(handler: Callable[[Union[str, int], Any], None]) -> None
on_keydown(handler: Callable[[Any, Union[str, int]], None]) -> None
on_open_menu(handler: Callable[[Union[str, int]], None]) -> None
css() -> str
css(value: str) -> None
data() -> List[Dict[str, Any]]
data(value: List[Dict[str, Any]]) -> None
menu_css() -> str
menu_css(value: str) -> None
navigation_type() -> str
navigation_type(value: str) -> None
```
