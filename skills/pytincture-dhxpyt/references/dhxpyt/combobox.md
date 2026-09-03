# dhxpyt.combobox

Generated from dhxpyt 0.9.18 source by `scripts/generate_reference.py`.

## Config classes

### ComboboxConfig
Configuration class for Combobox.

```python
ComboboxConfig(
    css: str = None,
    data: List[Dict[str, Any]] = None,
    disabled: bool = False,
    eventHandlers: Dict[str, Dict[str, Callable[[Any, Union[str, int]], Union[bool, None]]]] = None,
    filter: Callable[[Dict[str, Any], str], bool] = None,
    helpMessage: str = None,
    hiddenLabel: bool = False,
    htmlEnable: bool = False,
    itemHeight: Union[int, str] = 32,
    itemsCount: Union[bool, Callable[[int], str]] = False,
    label: str = None,
    labelPosition: str = 'top',
    labelWidth: Union[str, int] = 'auto',
    listHeight: Union[int, str] = 224,
    multiselection: bool = False,
    newOptions: bool = False,
    placeholder: str = None,
    readOnly: bool = False,
    selectAllButton: bool = False,
    template: Callable[[Any], str] = None,
    value: Union[str, int, List[Union[str, int]]] = None,
    virtual: bool = False,
)
```

## Widget classes

### Combobox

```python
add_option(value: Union[Dict[str, Any], str], join: bool = True) -> None
blur() -> None
clear() -> None
destructor() -> None
disable() -> None
enable() -> None
focus() -> None
get_value(as_array: bool = False) -> Union[str, int, List[Union[str, int]]]
is_disabled() -> bool
paint() -> None
set_value(ids: Union[str, int, List[Union[str, int]]]) -> None
add_event_handler(event_name: str, handler: Callable) -> None
on_after_close(handler: Callable[[], None]) -> None
on_after_open(handler: Callable[[], None]) -> None
on_before_change(handler: Callable[[Union[str, int, List[Union[str, int]]]], Union[bool, None]]) -> None
on_before_close(handler: Callable[[], Union[bool, None]]) -> None
on_before_open(handler: Callable[[], Union[bool, None]]) -> None
on_blur(handler: Callable[[], None]) -> None
on_change(handler: Callable[[Union[str, int, List[Union[str, int]]]], None]) -> None
on_focus(handler: Callable[[], None]) -> None
on_input(handler: Callable[[str], None]) -> None
on_keydown(handler: Callable[[Any, Union[str, int, None]], None]) -> None
css() -> str
css(value: str) -> None
data() -> List[Dict[str, Any]]
data(value: List[Dict[str, Any]]) -> None
disabled() -> bool
disabled(value: bool) -> None
multiselection() -> bool
multiselection(value: bool) -> None
placeholder() -> str
placeholder(value: str) -> None
read_only() -> bool
read_only(value: bool) -> None
value() -> Union[str, int, List[Union[str, int]]]
value(ids: Union[str, int, List[Union[str, int]]]) -> None
filter() -> Callable[[Dict[str, Any], str], bool]
filter(value: Callable[[Dict[str, Any], str], bool]) -> None
template() -> Callable[[Any], str]
template(value: Callable[[Any], str]) -> None
```
