# dhxpyt.toolbar

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### ButtonConfig

```python
ButtonConfig(
    id: Optional[str] = None,
    value: Optional[str] = None,
    circle: Optional[bool] = None,
    color: Optional[str] = None,
    count: Optional[int] = None,
    countColor: Optional[str] = None,
    full: Optional[bool] = None,
    group: Optional[str] = None,
    hotkey: Optional[str] = None,
    html: Optional[str] = None,
    icon: Optional[str] = None,
    loading: Optional[bool] = None,
    multiClick: Optional[bool] = None,
    size: Optional[str] = None,
    tooltip: Optional[str] = None,
    view: Optional[str] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    hidden: Optional[bool] = None,
)
```

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

### DatePickerConfig

```python
DatePickerConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    value: Optional[str] = None,
    valueFormat: Optional[str] = None,
    dateFormat: Optional[str] = '%d/%m/%y',
    disabledDates: Optional[List[Dict[str, str]]] = None,
    icon: Optional[str] = None,
    label: Optional[str] = None,
    mark: Optional[str] = None,
    mode: Optional[str] = None,
    placeholder: Optional[str] = None,
    thisMonthOnly: Optional[bool] = None,
    timeFormat: Optional[str] = None,
    timePicker: Optional[bool] = None,
    weekNumbers: Optional[bool] = None,
    weekStart: Optional[int] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    editable: Optional[bool] = None,
    hidden: Optional[bool] = None,
    width: Optional[Union[int, str]] = None,
)
```

### ImageButtonConfig

```python
ImageButtonConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    src: Optional[str] = None,
    count: Optional[int] = None,
    countColor: Optional[str] = None,
    group: Optional[str] = None,
    hotkey: Optional[str] = None,
    multiClick: Optional[bool] = None,
    tooltip: Optional[str] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    hidden: Optional[bool] = None,
)
```

### InputConfig

```python
InputConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    value: Optional[str] = None,
    autocomplete: Optional[bool] = False,
    icon: Optional[str] = None,
    label: Optional[str] = None,
    placeholder: Optional[str] = None,
    tooltip: Optional[str] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    hidden: Optional[bool] = None,
    width: Optional[Union[int, str]] = None,
)
```

### MenuItemConfig

```python
MenuItemConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    value: Optional[str] = None,
    items: Optional[List['MenuItemConfig']] = None,
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

### SeparatorConfig

```python
SeparatorConfig(
    id: Optional[str] = None,
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

### ToolbarConfig
Configuration class for the Toolbar widget.

```python
ToolbarConfig(
    data: Optional[List[ControlConfig]] = None,
    css: Optional[str] = None,
    menuCss: Optional[str] = None,
    navigationType: Optional[str] = 'click',
)
```

## Widget classes

### Toolbar

```python
destructor() -> None
disable(ids: Union[str, int, List[Union[str, int]]] = None) -> None
enable(ids: Union[str, int, List[Union[str, int]]] = None) -> None
get_selected() -> List[Union[str, int]]
get_state(id: Union[str, int] = None) -> Union[str, bool, dict]
hide(ids: Union[str, int, List[Union[str, int]]] = None) -> None
is_disabled(id: Union[str, int]) -> bool
is_selected(id: Union[str, int]) -> bool
paint() -> None
select(id: Union[str, int], unselect: bool = True) -> None
set_focus(id: Union[str, int]) -> None
set_state(state: dict) -> None
update_item(id, item_dict: str) -> None
show(ids: Union[str, int, List[Union[str, int]]] = None) -> None
unselect(id: Union[str, int] = None) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_hide(handler: Callable[[Any], None]) -> None
on_before_hide(handler: Callable[[Union[str, int], Any], Union[bool, None]]) -> None
on_click(handler: Callable[[Union[str, int], Any], None]) -> None
on_input(handler: Callable[[str, str], None]) -> None
on_input_blur(handler: Callable[[Union[str, int]], None]) -> None
on_input_change(handler: Callable[[Union[str, int], str], Any]) -> None
on_input_created(handler: Callable[[Union[str, int], Any], None]) -> None
on_input_focus(handler: Callable[[Union[str, int]], None]) -> None
on_keydown(handler: Callable[[Any, Optional[str]], None]) -> None
on_open_menu(handler: Callable[[Union[str, int]], None]) -> None
```
