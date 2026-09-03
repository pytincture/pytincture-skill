# dhxpyt.ribbon

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### BlockConfig

```python
BlockConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    items: Optional[List['ControlConfig']] = None,
    direction: Optional[str] = None,
    title: Optional[str] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    hidden: Optional[bool] = None,
)
```

### ButtonConfig

```python
ButtonConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    value: Optional[str] = None,
    items: Optional[List['ControlConfig']] = None,
    active: Optional[bool] = None,
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
    twoState: Optional[bool] = None,
    view: Optional[str] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    hidden: Optional[bool] = None,
)
```

### ControlConfig

_No keyword parameters._

### CustomHTMLButtonConfig

```python
CustomHTMLButtonConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    html: Optional[str] = None,
    css: Optional[str] = None,
    hidden: Optional[bool] = None,
)
```

### DatepickerConfig

```python
DatepickerConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    value: Optional[str] = None,
    valueFormat: Optional[str] = None,
    dateFormat: Optional[str] = None,
    disabledDates: Optional[List[Any]] = None,
    icon: Optional[str] = None,
    label: Optional[str] = None,
    mark: Optional[List[Any]] = None,
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
    width: Optional[int] = None,
)
```

### ImageButtonConfig

```python
ImageButtonConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    src: str = None,
    active: Optional[bool] = None,
    count: Optional[int] = None,
    countColor: Optional[str] = None,
    group: Optional[str] = None,
    hotkey: Optional[str] = None,
    size: Optional[str] = None,
    tooltip: Optional[str] = None,
    twoState: Optional[bool] = None,
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
    icon: Optional[str] = None,
    label: Optional[str] = None,
    placeholder: Optional[str] = None,
    tooltip: Optional[str] = None,
    width: Optional[int] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    hidden: Optional[bool] = None,
)
```

### NavItemConfig

```python
NavItemConfig(
    type: Optional[str] = 'navItem',
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
    size: Optional[str] = None,
    tooltip: Optional[str] = None,
    twoState: Optional[bool] = None,
    css: Optional[str] = None,
    disabled: Optional[bool] = None,
    hidden: Optional[bool] = None,
)
```

### RibbonConfig
Configuration class for the Ribbon widget.

```python
RibbonConfig(
    data: Optional[List[ControlConfig]] = None,
    css: Optional[str] = None,
    menuCss: Optional[str] = None,
)
```

### SelectButtonConfig

```python
SelectButtonConfig(
    id: Optional[str] = None,
    parent: Optional[str] = None,
    value: Optional[str] = None,
    items: Optional[List['ControlConfig']] = None,
    count: Optional[int] = None,
    countColor: Optional[str] = None,
    icon: Optional[str] = None,
    size: Optional[str] = None,
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

## Widget classes

### Ribbon

```python
destructor() -> None
disable(ids: Union[str, int, List[Union[str, int]]] = None) -> None
enable(ids: Union[str, int, List[Union[str, int]]] = None) -> None
get_selected() -> List[Union[str, int]]
get_state() -> Dict[str, Any]
hide(ids: Union[str, int, List[Union[str, int]]] = None) -> None
is_disabled(id: Union[str, int]) -> bool
is_selected(id: Union[str, int]) -> bool
paint() -> None
select(id: Union[str, int], unselect: bool = True) -> None
set_state(state: Dict[str, Any]) -> None
show(ids: Union[str, int, List[Union[str, int]]] = None) -> None
unselect(id: Union[str, int] = None) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_click(handler: Callable[[Union[str, int], Any], None]) -> None
on_input(handler: Callable[[str, str], None]) -> None
on_input_blur(handler: Callable[[Union[str, int]], None]) -> None
on_input_change(handler: Callable[[Union[str, int], str], None]) -> None
on_input_created(handler: Callable[[Union[str, int], Any], None]) -> None
on_input_focus(handler: Callable[[Union[str, int]], None]) -> None
on_keydown(handler: Callable[[Any, Optional[str]], None]) -> None
on_open_menu(handler: Callable[[Union[str, int]], None]) -> None
```
